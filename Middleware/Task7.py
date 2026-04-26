def decorator(func):
    def wrapper():
        return func()
    return wrapper


@decorator
def test():
    pass

print(test.__name__)  # wrapper

#Fix

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper