from typing import Any

from fastapi import APIRouter, BackgroundTasks, Depends, Response, status

from src.auth import jwt, service, utils
from src.auth.dependencies import (valid_refresh_token,
                                   valid_refresh_token_user, valid_user_create)
from src.auth.jwt import parse_jwt_user_data
from src.auth.schemas import (AccessTokenResponse, AuthUser, JWTData,
                              UserResponse)

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user(
    auth_data: AuthUser = Depends(valid_user_create),
) -> dict[str, str]:
    user = await service.create_user(auth_data)
    return {
        "email": user["email"],  # type: ignore
    }


@router.get("/users/me", response_model=UserResponse)
async def get_my_account(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
) -> dict[str, str]:
    user = await service.get_user_by_id(jwt_data.user_id)
    return {
        "email": user["email"],
    }


@router.put("/users/tokens", response_model=AccessTokenResponse)
async def refresh_token(
    worker: BackgroundTasks,
    response: Response,
    refresh_token: dict[str, Any] = Depends(valid_refresh_token),
    user: dict[str, Any] = Depends(valid_refresh_token_user),
) -> AccessTokenResponse:
    refresh_token_value = await service.create_refresh_token(
        user_id=refresh_token["user_id"]
    )
    response.set_cookie(**utils.get_refresh_token_settings(refresh_token_value))
    worker.add_task(service.expire_refresh_token, refresh_token["uuid"])
    return AccessTokenResponse(
        access_token=jwt.create_access_token(user=user),
        refresh_token=refresh_token,
    )


@router.post("/users/tokens", response_model=AccessTokenResponse)
async def auth_user(auth_data: AuthUser, response: Response) -> AccessTokenResponse:
    user = await service.authenticate_user(auth_data)
    refresh_token = await service.create_refresh_token(user_id=user["id"])
    access_token = jwt.create_access_token(user=user)
    response.set_cookie(**utils.get_refresh_token_settings(refresh_token))
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        domain="localhost",
    )
    return AccessTokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.delete("/users/tokens")
async def logout_user(
    response: Response,
    refresh_token: dict[str, Any] = Depends(valid_refresh_token),
) -> None:
    await service.expire_refresh_token(refresh_token["uuid"])

    response.delete_cookie(
        **utils.get_refresh_token_settings(refresh_token["refresh_token"], expired=True)
    )
