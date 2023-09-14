from functools import wraps
from typing import Type

from database.base import BaseAccessor


def get_accessor(accessor: Type[BaseAccessor]):
    def outer(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            accessor_instance = accessor()
            await func(*args, accessor=accessor_instance, **kwargs)
            await accessor_instance.session.close()

        return wrapper

    return outer
