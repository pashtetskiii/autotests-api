from pydantic import BaseModel, ConfigDict, EmailStr, constr
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class UserSchema(BaseSchema):
    id: str
    email: EmailStr
    last_name: constr(min_length=1, max_length=50)
    first_name: constr(min_length=1, max_length=50)
    middle_name: constr(min_length=1, max_length=50)


class CreateUserRequestSchema(BaseSchema):
    email: EmailStr
    password: constr(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50)
    first_name: constr(min_length=1, max_length=50)
    middle_name: constr(min_length=1, max_length=50)


class CreateUserResponseSchema(BaseSchema):
    user: UserSchema
