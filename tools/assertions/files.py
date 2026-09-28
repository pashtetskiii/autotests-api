from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.base import assert_equal


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    '''
    Проверяет, что ответ на создание файла соотвествует запросу
    :param request: Исохдный запрос на создание файла.
    :param response: Отвт API с данными файла.
    :return: Если хотя бы одно поле не совпадает.
    '''
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")
    assert_equal(str(response.file.url), expected_url, "url")

def assert_file(actual: FileSchema, expected: FileSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")

def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    assert_file(get_file_response.file, create_file_response.file)