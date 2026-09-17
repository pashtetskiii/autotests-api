from pydantic import BaseModel, Field

class ContactSchema(BaseModel):
    full_name: str = Field(alias="fullName")

ContactSchema(fullName="Лев Толстой")
ContactSchema(full_name="Лев Толстой")