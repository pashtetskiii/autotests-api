from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class ExerciseSchema(BaseSchema):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExercisesQuerySchema(BaseSchema):
    """
    Описание структуры запроса на получение списка заданий.
    """
    course_id: str


class GetExercisesResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения списка заданий.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseSchema):
    """
    Описание структуры ответа получения задания.
    """
    exercise: ExerciseSchema


class CreateExerciseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class CreateExerciseResponseSchema(BaseSchema):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None = None
    max_score: int | None = None
    min_score: int | None = None
    order_index: int | None = None
    description: str | None = None
    estimated_time: str | None = None


class UpdateExerciseResponseSchema(BaseSchema):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema
