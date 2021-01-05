from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

# Define types using Schema Definition Language (https://graphql.org/learn/schema/)
# Wrapping string in gql function provides validation and better error traceback
type_defs = gql(
    """
    type Query {
        user: [User!]!
    }

    type User {
        firstName: String
        lastName: String
        email: String
        fullName: String
    }
"""
)

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Resolvers are simple python functions
@query.field("user")
async def resolve_user(*_):
    return [
        {"firstName": "John", "lastName": "Doe", "email": "Jhon@gmail.com"},
        {"firstName": "Bob", "lastName": "Boberson", "eamil": "Bob@gmail.com"},
    ]


# Map resolver functions to custom type fields using ObjectType
user = ObjectType("User")


@user.field("fullName")
async def resolve_user_fullname(user, *_):
    return "%s %s" % (user["firstName"], user["lastName"])


# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, user)
