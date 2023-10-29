from pydantic import BaseModel

from src.module.api.enviroment_utils.properties_utils import PropertiesUtils


class User(BaseModel):
    login: str
    password: str

    def __str__(self):
        return self.model_dump_json()


ADMIN_USER = User(login="admin", password="password")


def create_session(user: User):
    return f'{user.login}_session_<server_name>_value'


def fixture_admin_session():
    env_prop_value = PropertiesUtils.get_properties_value('session_<server_name>_admin')
    return env_prop_value if env_prop_value else create_session(ADMIN_USER)


prop_name = "test_user1"

print(f'prop name after PropertiesUtils.append_server(name): {PropertiesUtils.append_server(prop_name)}')
result = PropertiesUtils.get_properties_value(prop_name)
print(f'get 1: {result}')

PropertiesUtils.set_properties_value(prop_name, ADMIN_USER.model_dump())

result = PropertiesUtils.get_properties_value(prop_name)
print(f'get 2: {result}')

result = PropertiesUtils.get_prop_typed_value(prop_name, User)

print(f'check type: {type(result)}')
print(f'print value: {result}')

PropertiesUtils.delete_property(prop_name)

result = PropertiesUtils.get_properties_value(prop_name)
print(f'get 3: {result}')
