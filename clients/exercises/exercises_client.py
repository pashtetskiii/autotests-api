from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь с courseId — идентификатором курса, для которого
            запрашивается список заданий.
        :return: Объект Response с данными ответа (список заданий курса).
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения информации о задании по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Объект Response с данными ответа (данные задания).
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с данными для создания задания:
            title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Объект Response с данными ответа (созданное задание).
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления данных задания по exercise_id.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с данными для обновления задания:
            title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Объект Response с данными ответа (обновленное задание).
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по exercise_id.

        :param exercise_id: Идентификатор задания.
        :return: Объект Response с данными ответа.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
