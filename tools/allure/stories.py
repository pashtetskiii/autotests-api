from enum import Enum

class AllureStory(str, Enum):
    LOGIN = "LOGIN"

    GET_ENTITY = "Get entities"
    GET_ENTITIES = "Get entities"
    CREATE_ENTITY = "Create entities"
    UPDATE_ENTITY = "Update entities"
    DELETE_ENTITY = "Delete entities"
    VALIDATE_ENTITY = "Validate entities"