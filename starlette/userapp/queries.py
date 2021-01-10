from userapp.models import users
from database import database
from starlette.authentication import has_required_scope
from graphql.type.definition import GraphQLResolveInfo


async def resolve_user(_: any, info: GraphQLResolveInfo):
    request = info.context["request"]
    if not has_required_scope(request, ["authenticated"]):
        print("======================")
        return {
            "status": 403,
            "error": {"code": 403, "message": "Forbidden"},
            "user": [],
        }
    query = users.select()
    results = await database.fetch_all(query)
    content = [
        {
            "id": result["id"],
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
