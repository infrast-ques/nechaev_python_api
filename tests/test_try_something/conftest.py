import allure
import pytest

from src.module.fixture_utils.entity_cleanup_expressions import EntityCleanupFunctions
from src.module.fixture_utils.thread_safety_entity_utils import get_local_thread


@pytest.fixture(scope='function', autouse=True)
def clear_data_after_test():
    yield
    with allure.step('teardown fixture'):
        print('teardown fixture from thread')
        test_entities_list = get_local_thread()
        for entity in test_entities_list:
            if entity['key'] in EntityCleanupFunctions.list_names():
                EntityCleanupFunctions.get_function(entity['key'])(entity['values'])
