from src.messages.schemas import Message
from databases.interfaces import Record


def map_messages(data: Record | None) -> list[Message]:
    rows = [dict(row) for row in data]
    return [
        Message(
            message=row["message"],
            created_at=row["created_at"],
            sender=row["sender"],
        )
        for row in rows
    ]
