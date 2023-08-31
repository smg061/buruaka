from datetime import datetime

from src.models import ORJSONModel


class Message(ORJSONModel):
    message: str
    created_at: datetime
    sender: str

    class Config:
        from_attributes = True


class Messages(ORJSONModel):
    messages: list[Message]

    class Config:
        from_attributes = True


class StudentMessageCreate(ORJSONModel):
    message: str
    student_id: int
    message_type: str = "text"
    is_read: bool = False

    class Config:
        from_attributes = True


class StudentMessageCount(ORJSONModel):
    count: int

    class Config:
        from_attributes = True
