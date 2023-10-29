import threading

import allure

local_thread = threading.local()


def get_local_thread():
    if not hasattr(local_thread, 'value'):
        local_thread.value = list()
    return local_thread.value


def add_to_local_thread(new_value):
    if not hasattr(local_thread, 'value'):
        local_thread.value = list()
    return local_thread.value.append(new_value)


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
