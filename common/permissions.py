from typing import Any

from strawberry import BasePermission
from strawberry.types import Info


class OnlyLoggedIn(BasePermission):
    message = "You need to be logged in for this!"

    def has_permission(self, source: Any, info: Info, **kwargs):
        return info.context.request.user.is_authenticated
