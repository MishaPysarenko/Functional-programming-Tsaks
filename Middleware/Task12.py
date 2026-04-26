def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return "Something went wrong"
    return wrapper


@handle_errors
def divide(a, b):
    return a / b