from todo.models import todo
from database import database


async def resolve_create_todo(_, info, input):
    try:
        query = todo.insert().values(
            title=input["title"],
            description=input["description"],
            author_id=input["author_id"],
        )
        result = await database.execute(query)

        payload = {
            "success": True,
            "record": {
                "id": result,
                "title": input["title"],
                "description": input["description"],
                "author_id": input["author_id"],
            },
        }
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}

    return payload
