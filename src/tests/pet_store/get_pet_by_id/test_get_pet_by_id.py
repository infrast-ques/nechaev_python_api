from src.module.api.clients.clients import api_client_pet_store
from src.module.utils.deserializer.deserialize import serialize
from src.module.api.requests.pet_store.models.request.AddPetRequest import AddPetRequest
from src.module.api.requests.pet_store.requests.PetStoreRequests import PetStoreRequests


def test_get_pet_by_id():
    expected_pet_data = AddPetRequest(id=11111)
    api_client_pet_store.send_request(PetStoreRequests.pet_add(expected_pet_data))

    response_api = api_client_pet_store.send_request(PetStoreRequests.pet_get_by_id(11111))

    assert response_api.response_dict_body == serialize(expected_pet_data)
