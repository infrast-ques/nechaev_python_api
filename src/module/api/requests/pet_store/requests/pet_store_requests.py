from src.module.api.requests.HTTPMethod import HTTPMethod
from src.module.api.requests.Request import TRequest
from src.module.api.requests.pet_store.models.response.GetPetResponse import GetPetResponse


class PetStoreRequests:

    @staticmethod
    def petGetById(pet_id: int) -> TRequest:
        return TRequest(
            response_type=GetPetResponse,
            method=HTTPMethod.GET,
            endpoint=f"/v2/pet/{pet_id}"
        )
