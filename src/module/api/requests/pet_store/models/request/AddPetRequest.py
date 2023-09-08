import random
import sys
from dataclasses import dataclass, field
from typing import List

from src.module.utils.Utils import Utils


@dataclass
class Category:
    id: int = random.randint(1, sys.maxsize)
    name: str = f'category_name_{Utils.get_random_string(50)}'


@dataclass
class Tag:
    id: int = random.randint(1, sys.maxsize)
    name: str = f'tag_name_{Utils.get_random_string(50)}'


@dataclass
class AddPetRequest:
    id: int
    name: str = f'name_{Utils.get_random_string(50)}'
    category: Category = field(default_factory=lambda: (Category()))
    photoUrls: List[str] = (f'photo_url_{Utils.get_random_string(50)}',
                            f'photo_url_{Utils.get_random_string(50)}')
    tags: List[Tag] = field(default_factory=lambda: (Tag(),
                                                     Tag()))
    status: str = f'status_{Utils.get_random_string(10)}'
