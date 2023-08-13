import mimetypes

from src.module.api.requests.implementation.HTTPMethod import HTTPMethod
from src.module.api.requests.implementation.TRequest import TRequest
from src.module.api.requests.pet_store.models.request.AddPetRequest import AddPetRequest
from src.module.api.requests.pet_store.models.response.GetPetResponse import GetPetResponse
from src.module.utils.deserializer.deserialize import serialize


class PetStoreRequests:

    @staticmethod
    def pet_get_by_id(pet_id: int) -> TRequest:
        return TRequest(
            response_type=GetPetResponse,
            method=HTTPMethod.GET,
            endpoint=f'/v2/pet/{pet_id}'
        )

    @staticmethod
    def pet_add(data: AddPetRequest) -> TRequest:
        return TRequest(
            response_type=GetPetResponse,
            method=HTTPMethod.POST,
            content_type=mimetypes.types_map['.json'],
            body=serialize(data),
            endpoint='/v2/pet'
        )
