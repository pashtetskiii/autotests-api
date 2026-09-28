from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.assertions.base import assert_equal


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")
    assert_equal(str(response.file.url), expected_url, "url")