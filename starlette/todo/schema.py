from ariadne import (
    gql,
    make_executable_schema,
    ObjectType,
)

from todo.queries import resolve_todos, resolve_todo
from todo.mutations import (
    resolve_create_todo,
)

type_defs = gql(
    """
    type Todo {
        id: Int!
        title: String!
        description: String!
        created_on: String!
        author_id: Int!
    }

     type TodoResult {
        success: Boolean!
        errors: [String]
        todos: Todo
    }
    type TodosResult {
        success: Boolean!
        errors: [String]
        records: [Todo]
    }


    type DeleteTodoResult {
        success: Boolean!
        errors: [String]
    }



            input ToDoInput {
  id: Int!
title: String!
description: String!
created_on: String!
author_id: Int!
}


    type Query {
        todos: [Todo!]!
        todo(id:Int!): [Todo!]!
    }
    # type Mutation {
    #     createTodo(title: String!): TodoResult!
    #     deleteTodo(todoId: ID!): DeleteTodoResult!
    #     completeTodo(todoId: String!): TodoResult!
    # }



        type Mutation {
   createTodo(input: ToDoInput!): TodoResult!
}
"""
)

query = ObjectType("Query")

query.set_field("todos", resolve_todos)
query.set_field("todo", resolve_todo)

mutation = ObjectType("Mutation")
mutation.set_field("createTodo", resolve_create_todo)


schema = make_executable_schema(type_defs, query, mutation)
