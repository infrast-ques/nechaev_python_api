from src.module.api.clients.clients import api_client_pet_store
from src.module.api.requests.pet_store.models.request.AddPetRequest import AddPetRequest
from src.module.api.requests.pet_store.requests.PetStoreRequests import PetStoreRequests


def test_get_pet_by_id():
    expected_pet_data = AddPetRequest(id=11111)
    api_client_pet_store.send_request(PetStoreRequests.pet_add(expected_pet_data))
    print(11)
    response = api_client_pet_store.send_request(PetStoreRequests.pet_get_by_id(11111))
    print(111)
    assert response.status_code == 200
    print(1111)
    # assert response.response_dict_body == expected_pet_data.__dict__
