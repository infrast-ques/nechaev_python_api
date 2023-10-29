from enum import Enum
from typing import List

from src.module.fixture_utils.thread_safety_entity_storage import delete_user, delete_role


class EntityCleanupFunctions(Enum):
    USER = ('user', delete_user)
    ROLE = ('role', delete_role)

    def __init__(self, entity_name: str, function: callable):
        self.entity_name = entity_name
        self.function = function

    @classmethod
    def list(cls) -> List[Enum]:
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_names(cls) -> List[str]:
        return list(map(lambda c: c.value[0], cls))

    @classmethod
    def get_function(cls, entity_name: str) -> callable:
        for item in cls.list():
            if item[0] == entity_name:
                return item[1]
