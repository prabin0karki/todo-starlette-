from ariadne import (
    gql,
    make_executable_schema,
    ObjectType,
)

from userapp.queries import (
    resolve_user,
    resolve_user_fullname,
)

from userapp.mutations import (
    resolve_register,
    resolve_login,
)

type_defs = gql(
    """
    type User {
        id: Int!
        first_name: String
        last_name: String
        email: String
        full_name: String
        password: String
    }
    type UserResult {
        success: Boolean!
        errors: [String]
        user: User
    }
    type AuthResult {
        success: Boolean!
        errors: [String]
        token: String
    }


    input UserInput {
        first_name: String
        last_name: String
        email: String
        password: String
}

    input LoginInput {
  email: String
  password: String
}

    type Query {
        user: [User!]!
    }

    type Mutation {
  createUser(input: UserInput!): UserResult!
  login(input: LoginInput!): AuthResult!
}


"""
)


query = ObjectType("Query")
user = ObjectType("User")

query.set_field("user", resolve_user)
user.set_field("full_name", resolve_user_fullname)
mutation = ObjectType("Mutation")
mutation.set_field("createUser", resolve_register)
mutation.set_field("login", resolve_login)


schema = make_executable_schema(type_defs, query, mutation)
