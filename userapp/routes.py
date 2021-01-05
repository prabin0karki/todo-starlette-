from userapp import views
from starlette.routing import Route
from ariadne.asgi import GraphQL
from ariadne import make_executable_schema
from userapp.schemas import schema

routes = [
    # Route("/", views.home, name="home"),
    Route("/graphql", GraphQL(schema, debug=True))
]
