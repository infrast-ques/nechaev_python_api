import json
import os
from typing import TypeVar

import pytest


class PropertiesUtils:
    BASE_ENTITY_PREFIX_SET = {'TEST_SESSION', 'TEST_USER', 'TEST_ROLE'}
    type = TypeVar("type")

    @staticmethod
    def get_test_thread_server_name():
        return "server_name"  # пока что хз как это сделать

    @staticmethod
    def append_server(prop_name):
        return f'{prop_name}_{PropertiesUtils.get_test_thread_server_name()}'.upper()

    @staticmethod
    def get_properties_value(name: str) -> str:
        return os.getenv(PropertiesUtils.append_server(name))

    @staticmethod
    def get_prop_typed_value(name: str, deserializable_type: type) -> type:
        env_value = PropertiesUtils.get_properties_value(name)
        env_value_dict = json.loads(env_value)
        return deserializable_type(**env_value_dict)

    @staticmethod
    def set_properties_value(name: str, value: str | dict):
        if isinstance(value, str):
            os.environ[PropertiesUtils.append_server(name)] = str(value)
        elif isinstance(value, dict):
            os.environ[PropertiesUtils.append_server(name)] = json.dumps(value)

    @staticmethod
    def delete_property(name):
        try:
            del os.environ[PropertiesUtils.append_server(name)]
        except:
            pass

    @pytest.fixture(scope='session', autouse=True)
    def delete_properties(self):
        prop_set = set(filter(
            lambda key: any(key.startswith(prefix) for prefix in self.BASE_ENTITY_PREFIX_SET),
            os.environ.keys()))
        [PropertiesUtils.delete_property(prop) for prop in prop_set]
