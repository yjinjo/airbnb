import strawberry
from django.conf import settings
from strawberry import auto
from . import models
from users.types import UserType
from typing import List
from reviews.types import ReviewType


@strawberry.django.type(models.Room)
class RoomType:
    id: auto
    name: auto
    kind: auto
    owner: "UserType"

    @strawberry.field
    def reviews(self, page: int) -> List["ReviewType"]:
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        return self.reviews.all()[start:end]
