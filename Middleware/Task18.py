def to_uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper


@to_uppercase_result
def greet(name):
    return f"Hello, {name}"