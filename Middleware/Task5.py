def positive_only(func):
    def wrapper(*args):
        if any(a < 0 for a in args if isinstance(a, (int, float))):
            return "Error: negative value"
        return func(*args)
    return wrapper


@positive_only
def multiply(a, b):
    return a * b