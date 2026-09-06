from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema


class BaseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class CourseSchema(BaseSchema):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema  # Вложенная структура файла
    estimated_time: str
    created_by_user: UserSchema  # Вложенная структура пользователя


class GetCoursesQuerySchema(BaseSchema):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str


class CreateCourseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str


class CreateCourseResponseSchema(BaseSchema):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None = None
    max_score: int | None = None
    min_score: int | None = None
    description: str | None = None
    estimated_time: str | None = None
