from starlette.routing import Route
from ariadne.asgi import GraphQL
from ariadne import make_executable_schema
from todo.schema import schema

# from userapp.views import user_note

# mutation.set_field("login", auth_mutations.resolve_login)
# mutation.set_field("logout", auth_mutations.resolve_logout)


routes = [
    # Route("/", views.home, name="home"),
    Route("/todo", GraphQL(schema, debug=True)),
    # Route("/users", GraphQL(schema1, debug=True), methods=["POST"]),
]
