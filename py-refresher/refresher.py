from typing import Callable
from functools import wraps

def decorator_factory(access_level):
    @wraps(func)
    def decorator(func: Callable) -> Callable:     
        def inner(*args, *kwargs):
            return func(*args, **kwargs)
        return inner
    return decorator    



@decorator_factory("admin")
def get_admin_password(name: str) -> str:
    return "1234"


@decorator_factory("user")
def get_user_password(name: str) -> str:
    return "5678"