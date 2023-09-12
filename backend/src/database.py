from typing import Any

from sqlalchemy import (Boolean, Column, CursorResult, DateTime, Enum,
                        ForeignKey, Identity, Insert, Integer, LargeBinary,
                        MetaData, Select, String, Update, func, text)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings
from src.constants import DB_NAMING_CONVENTION

DATABASE_URL = str(settings.DATABASE_URL)
engine = create_async_engine(DATABASE_URL)
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)


class Base(DeclarativeBase):
    __abstract__ = True
    metadata = metadata


class AuthUser(Base):
    __tablename__ = "auth_user"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    email = Column(String, nullable=False)
    password = Column(LargeBinary, nullable=False)
    is_admin = Column(Boolean, server_default="false", nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class RefreshToken(Base):
    __tablename__ = "auth_refresh_token"
    metadata = metadata
    uuid = Column(UUID, primary_key=True)
    user_id = Column(ForeignKey("auth_user.id", ondelete="CASCADE"), nullable=False)
    refresh_token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class Student(Base):
    __tablename__ = "students"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    profile_picture = Column(String, nullable=False)
    sprite = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    relationship_level = Column(Integer, default=1, server_default="1", nullable=False)
    profile_message = Column(String, nullable=False)
    dob = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class StudentPhrase(Base):
    __tablename__ = "student_phrases"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    student_id = Column(ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    phrase = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class SenseiMessage(Base):
    __tablename__ = "sensei_messages"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    student_id = Column(
        ForeignKey("students.id", ondelete="CASCADE"), index=True, nullable=False
    )
    message = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class StudentMessage(Base):
    __tablename__ = "student_messages"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    student_id = Column(
        ForeignKey("students.id", ondelete="CASCADE"), index=True, nullable=False
    )
    message = Column(String, nullable=False)
    is_read = Column(
        Boolean, server_default="false", index=True, default=False, nullable=False
    )
    message_type = Column(
        Enum("text", "picture", name="message_type"),
        nullable=False,
        server_default="text",
        default="text",
        index=True,
    )
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class GroupChat(Base):
    __tablename__ = "group_chat"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class GroupChatMessage(Base):
    __tablename__ = "group_chat_message"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    group_chat_id = Column(
        ForeignKey("group_chat.id", ondelete="CASCADE"), index=True, nullable=False
    )
    message = Column(String, nullable=False)
    is_read = Column(
        Boolean, server_default="false", index=True, default=False, nullable=False
    )
    message_type = Column(
        Enum("text", "picture", name="message_type"),
        nullable=False,
        server_default="text",
        default="text",
        index=True,
    )
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class GroupChatSenseiMessage(Base):
    __tablename__ = "group_chat_sensei_message"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    group_chat_id = Column(
        ForeignKey("group_chat.id", ondelete="CASCADE"), index=True, nullable=False
    )
    message = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class GroupChatMember(Base):
    __tablename__ = "group_chat_member"
    metadata = metadata
    id = Column(Integer, Identity(), primary_key=True)
    group_chat_id = Column(
        ForeignKey("group_chat.id", ondelete="CASCADE"), index=True, nullable=False
    )
    student_id = Column(
        ForeignKey("students.id", ondelete="CASCADE"), index=True, nullable=False
    )
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


async def fetch_one(
    select_query: Select | Insert | Update, values: dict[str, str] = None
) -> dict[str, Any] | None:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query, values)
        return cursor.first()._asdict() if cursor.rowcount > 0 else None


async def fetch_all(
    select_query: Select | Insert | Update, values: dict[str, str] = None
) -> list[dict[str, Any]]:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query, values)
        return [r._asdict() for r in cursor.all()]

async def fetch_raw(
    raw_query: str, values: dict[str, str] = None
) -> list[dict[str, Any]]:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(text(raw_query), values)
        return cursor.first()._asdict() if cursor.rowcount > 0 else None
    
async def fetch_raw_all(
    raw_query: str, values: dict[str, str] = None
) -> list[dict[str, Any]]:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(text(raw_query), values)
        return [r._asdict() for r in cursor.all()]
    
async def execute(select_query: Insert | Update) -> None:
    async with engine.begin() as conn:
        await conn.execute(select_query)
