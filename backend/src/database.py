from databases import Database
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Identity,
    Integer,
    LargeBinary,
    MetaData,
    String,
    Table,
    create_engine,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from src.config import settings
from src.constants import DB_NAMING_CONVENTION

DATABASE_URL = settings.DATABASE_URL.unicode_string()
engine = create_engine(DATABASE_URL)
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)

database = Database(DATABASE_URL, force_rollback=settings.ENVIRONMENT.is_testing)


auth_user = Table(
    "auth_user",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("email", String, nullable=False),
    Column("password", LargeBinary, nullable=False),
    Column("is_admin", Boolean, server_default="false", nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)

refresh_tokens = Table(
    "auth_refresh_token",
    metadata,
    Column("uuid", UUID, primary_key=True),
    Column("user_id", ForeignKey("auth_user.id", ondelete="CASCADE"), nullable=False),
    Column("refresh_token", String, nullable=False),
    Column("expires_at", DateTime, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)

students = Table(
    "students",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("profile_picture", String, nullable=False),
    Column("sprite", String, nullable=False),
    Column("phone_number", String, nullable=False),
    Column("relationship_level", Integer, default=1, server_default="1", nullable=False),
    Column("profile_message", String, nullable=False),
    Column("dob", DateTime, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)

student_phrases = Table(
    "student_phrases",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("student_id", ForeignKey("students.id", ondelete="CASCADE"), nullable=False),
    Column("phrase", String, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)

sensei_messages = Table(
    "sensei_messages",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column(
        "student_id",
        ForeignKey("students.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    ),
    Column("message", String, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)

student_messages = Table(
    "student_messages",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column(
        "student_id",
        ForeignKey("students.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    ),
    Column("message", String, nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)
