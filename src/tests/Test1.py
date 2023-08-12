from src.module.api.clients.pet_store.client import apiClientPetStore
from src.module.api.requests.pet_store.requests.pet_store_requests import PetStoreRequests

response = apiClientPetStore.send_request(PetStoreRequests.petGetById(111111))

print(response.response)
print(response.response_body)