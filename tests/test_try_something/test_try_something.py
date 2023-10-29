import allure
import pytest

from src.module.fixture_utils.thread_safety_entity_storage import get_local_thread, create_user, create_role


@pytest.fixture(scope='function')
def setup_fixture():
    with allure.step('setup fixture'):
        role = create_role()['values']['role_name']
        user = create_user(login='test_test', role=role)
    return {'user': user, 'role': role}


def test_listener_fixture1(setup_fixture):
    with allure.step('Start test'):
        print('Start test')
        print(get_local_thread())
    with allure.step('1 step'):
        print('1 step')
        print(setup_fixture['user'])
        print(setup_fixture['role'])
    with allure.step('End test'):
        print('End test')


def test_listener_fixture0():
    print(get_local_thread())
    user = create_user()
    role = create_role()
    print(get_local_thread())
    print(user)
    print(role)
    print(get_local_thread())
