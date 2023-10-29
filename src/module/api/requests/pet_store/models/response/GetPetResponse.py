from typing import List

from pydantic import BaseModel


class Category(BaseModel):
    name: str
    id: int


class GetPetResponse(BaseModel):
    photoUrls: List[str]
    name: str
    id: int
    category: Category
    tags: List[Category]
    status: str
