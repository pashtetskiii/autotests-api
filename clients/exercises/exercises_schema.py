from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from tools.fakers import fake


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
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(BaseSchema):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseSchema):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int | None = Field(default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(BaseSchema):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema