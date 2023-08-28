from src.models import ORJSONModel


class Student(ORJSONModel):
    first_name: str
    last_name: str
    email: str
    profile_picture: str
    sprite: str
