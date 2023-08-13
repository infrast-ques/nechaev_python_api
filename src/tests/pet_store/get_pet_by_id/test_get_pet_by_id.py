import pytest

from src.module.api.clients.clients import api_client_pet_store
from src.module.utils.deserializer.deserialize import serialize
from src.module.api.requests.pet_store.models.request.AddPetRequest import AddPetRequest
from src.module.api.requests.pet_store.requests.PetStoreRequests import PetStoreRequests


@pytest.fixture
def expected_pet_data():
    expected_pet_data = AddPetRequest(id=11111)
    api_client_pet_store.send_request(PetStoreRequests.pet_add(expected_pet_data))
    return expected_pet_data


@pytest.mark.pet_store
@pytest.mark.posisitve
def test_get_pet_by_id(expected_pet_data):
    response_api = api_client_pet_store.send_request(PetStoreRequests.pet_get_by_id(expected_pet_data.id))

    assert response_api.dict_body == serialize(expected_pet_data)
