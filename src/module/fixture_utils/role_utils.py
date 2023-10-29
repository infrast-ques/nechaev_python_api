import allure

from src.module.fixture_utils.thread_safety_entity_utils import add_to_local_thread


@allure.step("Создать роль")
def create_role(role_name: str = 'test_role'):
    print("Вызов апи для создания роли")
    role = {
        'key': 'role',
        'values': {'role_name': role_name}
    }
    add_to_local_thread(role)
    return role


@allure.step("Удалить роль")
def delete_role(data: dict):
    print(f'Вызов апи для удаления роли {data}')
