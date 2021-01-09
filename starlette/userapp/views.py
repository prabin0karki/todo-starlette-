import base64
import pdb
import hashlib, binascii, os
from userapp.models import users
from database import database


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")

    pwdhash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode("ascii")


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]

    pwdhash = hashlib.pbkdf2_hmac(
        "sha512", provided_password.encode("utf-8"), salt.encode("ascii"), 100000
    )
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")
    return pwdhash == stored_password


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
        if verify_password(user.get("password", None), password):
            return gen_token(email, password)
    except Exception as er:
        pass
    return None


def gen_token(email, password):
    token = base64.b64encode(bytes(f"{email}:{password}", encoding="ascii")).decode(
        "ascii"
    )
    return token
