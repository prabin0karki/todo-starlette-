from userapp.models import users
from database import database


async def resolve_user(*_):
    query = users.select()
    results = await database.fetch_all(query)
    content = [
        {
            "first_name": result["first_name"],
            "last_name": result["last_name"],
            "email": result["email"],
            "password": result["password"],
        }
        for result in results
    ]

    return content


async def resolve_user_fullname(user, *_):
    return "%s %s" % (user["first_name"], user["last_name"])
