from todo.models import todo
from database import database


async def resolve_todos(_, info):
    try:
        query = todo.select()
        results = await database.fetch_all(query)
        content = [
            {
                "id": result["id"],
                "title": result["title"],
                "created_on": result["created_on"],
                # "modified_on": result["modifed_on"],
                "description": result["description"],
            }
            for result in results
        ]
        payload = content
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload


async def resolve_todo(_, info, id):
    print("*************************")
    try:
        query = todo.select().where(todo.c.author_id == id)
        results = await database.fetch_all(query)
        content = [
            {
                "id": result["id"],
                "title": result["title"],
                "created_on": result["created_on"],
                # "modified_on": result["modifed_on"],
                "description": result["description"],
            }
            for result in results
        ]
        payload = content
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload
