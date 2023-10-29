import random
import sys
from typing import List

from pydantic import BaseModel, Field

from src.module.utils.Utils import Utils


class Category(BaseModel):
    id: int = Field(default_factory=lambda: random.randint(1, sys.maxsize))
    name: str = Field(default_factory=lambda: f'category_name_{Utils.get_random_string(50)}')


class Tag(BaseModel):
    id: int = Field(default_factory=lambda: random.randint(1, sys.maxsize))
    name: str = Field(default_factory=lambda: f'tag_name_{Utils.get_random_string(50)}')


class AddPetRequest(BaseModel):
    id: int
    name: str = f'name_{Utils.get_random_string(50)}'
    category: Category = Field(default_factory=lambda: (Category()))
    photoUrls: List[str] = [f'photo_url_{Utils.get_random_string(50)}',
                            f'photo_url_{Utils.get_random_string(50)}']
    tags: List[Tag] = Field(default_factory=lambda: [Tag(), Tag()])
    status: str = f'status_{Utils.get_random_string(10)}'
