import pytest

from src.module.api.clients.clients import api_client_pet_store
from src.module.api.requests.pet_store.models.request.AddPetRequest import AddPetRequest
from src.module.api.requests.pet_store.requests.PetStoreRequests import PetStoreRequests


@pytest.fixture
def expected_pet_data():
    expected_pet_data = AddPetRequest(id=11111)
    api_client_pet_store.send_request(PetStoreRequests.pet_add(expected_pet_data))
    return expected_pet_data


@pytest.mark.timeout(60)
@pytest.mark.pet_store
@pytest.mark.positive
def test_get_pet_by_id(expected_pet_data):
    response_api = api_client_pet_store.send_request(PetStoreRequests.pet_get_by_id(expected_pet_data.id))

    assert response_api.dict_body == expected_pet_data.model_dump()


@pytest.mark.parametrize("a,b,result",
                         [(1, 2, -1),
                          (1, -2, 3),
                          (0, 0, 0),
                          (-1, -100, 99),
                          (500, 0, 500)])
def test_random(a, b, result):
    assert a - b == result


@pytest.mark.positive
@pytest.mark.skip("ISSUE-938")
def test_for_skip():
    assert True == False
