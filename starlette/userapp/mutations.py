from userapp.models import users
from database import database
from userapp.views import authenticate_user, get_password_hash


async def resolve_register(_, info, input):
    try:
        password_hash = get_password_hash(input["password"])
        query = users.insert().values(
            first_name=input["first_name"],
            last_name=input["last_name"],
            email=input["email"],
            password=password_hash,
            is_active=True,
            disabled=False,
        )
        last_record_id = await database.execute(query)
        return {
            "success": True,
            "user": {
                "id": last_record_id,
                "first_name": input["first_name"],
                "last_name": input["last_name"],
                "email": input["email"],
            },
        }
    except Exception as err:
        return {
            "status": False,
            "error": err,
        }


async def resolve_login(_, info, input):
    try:
        token = authenticate_user(input["email"], input["password"])
        if token:
            payload = {"success": True, "token": token}
        else:
            payload = {"success": False, "errors": ["Incorrect username or password"]}

    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload
