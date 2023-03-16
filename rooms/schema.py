import strawberry
from typing import List
from . import types
from . import queries


@strawberry.type
class Query:
    all_rooms: List[types.RoomType] = strawberry.field(
        resolver=queries.get_all_rooms,
    )
