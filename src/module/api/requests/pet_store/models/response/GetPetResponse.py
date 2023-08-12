from typing import List

from marshmallow_dataclass import dataclass


@dataclass
class Category:
    name: str
    id: int


@dataclass
class GetPetResponse:
    photoUrls: List[str]
    name: str
    id: int
    category: Category
    tags: List[Category]
    status: str
