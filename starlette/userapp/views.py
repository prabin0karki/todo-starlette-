import base64
import pdb
import jwt
import hashlib, binascii, os
from userapp.models import users
from database import database

from starlette.config import Config
from passlib.context import CryptContext
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
config = Config(".env")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> str:
    return pwd_context.verify(plain_password, hashed_password)


def authentication_required(resolver):
    async def wrapper_func(source, info, **kwargs):
        request = info.context["request"]
        result = None
        # todo: else should throw error
        if request.user.is_authenticated:
            # kwargs["id"] = request.user.id
            result = await resolver(source, info, **kwargs)
        return result

    return wrapper_func


async def get_user(email):
    user = None
    query = users.select().where(users.c.email == email)
    result = await database.fetch_one(query)
    if result:
        user = {
            "id": result["id"],
            "email": result["email"],
            "password": result["password"],
        }
    return user


async def authenticate_user(email, password):
    try:
        user = await get_user(email)
        if user is None:
            return None

        # pdb.set_trace()
        if verify_password(password, user.get("password", None)):
            return create_access_token(email, password)
    except Exception as er:
        pass
    return None


def create_access_token(email, password):
    expire = datetime.utcnow() + timedelta(minutes=15)
    encoded_jwt = jwt.encode(
        {"email": email, "password": password, "exp": expire},
        config("SECRET_KEY"),
        algorithm=config("ALGORITHM"),
    )
    return encoded_jwt
