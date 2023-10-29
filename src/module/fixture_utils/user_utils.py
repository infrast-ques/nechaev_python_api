import allure

from src.module.fixture_utils.thread_safety_entity_utils import add_to_local_thread


@allure.step("Создать пользователя")
def create_user(login: str = 'test_user',
                password: str = 'test_password',
                role: str = 'admin'):
    print("Вызов апи для создания пользователя")
    user = {
        'key': 'user',
        'values': {
            'login': login,
            'password': password,
            'role': role
        }
    }
    add_to_local_thread(user)
    return user


@allure.step("Удалить пользователя")
def delete_user(data: dict):
    print(f'Вызов апи для удаления пользователя {data}')
