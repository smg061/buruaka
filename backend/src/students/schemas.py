from datetime import datetime
from typing import Optional

from src.models import ORJSONModel


class Student(ORJSONModel):
    id: int
    first_name: str
    last_name: str
    email: str
    profile_picture: str
    sprite: str
    dob: datetime
    profile_message: str
    relationship_level: int
    unread_messages: Optional[list[str]] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }


class StudentUpdate(ORJSONModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    profile_picture: Optional[str] = None
    sprite: Optional[str] = None
    profile_message: Optional[str] = None
    relationship_level: Optional[int] = None
    phone_number: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }


class StudentCreate(ORJSONModel):
    first_name: str
    last_name: str
    email: str
    profile_picture: str
    sprite: str
    dob: str
    profile_message: str
    relationship_level: int
    phone_number: str

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }
