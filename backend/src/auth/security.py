import bcrypt


def hash_password(password: str) -> bytes:
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def check_password(password: str, db_password: bytes) -> bool:
    pw = bytes(password, "utf-8")
    return bcrypt.checkpw(pw, db_password)
