import allure

@allure.step("Build api client")
def build_api_client():
        with allure.step("Get user authentication token"):
            ...

        with allure.step("Create new api client"):
            ...



@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ...


@allure.step("Deleting course")
def delete_course():
    ...

def test_feature():
    build_api_client()
    create_course(title="Python")
    delete_course()