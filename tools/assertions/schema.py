from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    '''
    Проверяет, соотвествует ли JSON-обьект (instance) заданной JSON-схеме (schema)
    :param instance: JSON-данные, которые нужно проверить
    :param schema: Ожидаемая JSON-схема
    :return: jsonchema.exceptions.ValidationError: Если instance не соответсвет schema
    '''
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )