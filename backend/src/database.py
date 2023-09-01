from databases import Database
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Identity,
    Integer,
    LargeBinary,
    MetaData,
    String,
    create_engine,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from src.config import settings
from src.constants import DB_NAMING_CONVENTION

DATABASE_URL = settings.DATABASE_URL.unicode_string()
engine = create_engine(DATABASE_URL)
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)

database = Database(DATABASE_URL, force_rollback=settings.ENVIRONMENT.is_testing)


Base = declarative_base()


class AuthUser(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, Identity(), primary_key=True)
    email = Column(String, nullable=False)
    password = Column(LargeBinary, nullable=False)
    is_admin = Column(Boolean, server_default="false", nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class RefreshToken(Base):
    __tablename__ = "auth_refresh_token"
    uuid = Column(UUID, primary_key=True)
    user_id = Column(ForeignKey("auth_user.id", ondelete="CASCADE"), nullable=False)
    refresh_token = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class Student(Base):
    __tablename__ = "students"
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
    id = Column(Integer, Identity(), primary_key=True)
    student_id = Column(ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    phrase = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class SenseiMessage(Base):
    __tablename__ = "sensei_messages"
    id = Column(Integer, Identity(), primary_key=True)
    student_id = Column(
        ForeignKey("students.id", ondelete="CASCADE"), index=True, nullable=False
    )
    message = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())


class StudentMessage(Base):
    __tablename__ = "student_messages"
    id = Column(Integer, Identity(), primary_key=True)
    student_id = Column(
        ForeignKey("students.id", ondelete="CASCADE"), index=True, nullable=False
    )
    message = Column(String, nullable=False)
    is_read = Column(Boolean, server_default="false", default=False, nullable=False)
    message_type = Column(
        Enum("text", "picture", name="message_type"),
        nullable=False,
        server_default="text",
        default="text",
    )
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
