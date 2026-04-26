def logger(func):
    def wrapper(*args, **kwargs):
        print("log")
        return func(*args, **kwargs)
    return wrapper


def require_auth(func):
    def wrapper(user, value):
        if not user.get("authenticated"):
            return "denied"
        return func(user, value)
    return wrapper


def validate_positive(func):
    def wrapper(user, value):
        if value < 0:
            return "invalid"
        return func(user, value)
    return wrapper


def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return "error"
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@logger
@timer
@handle_errors
@require_auth
@validate_positive
def handle_request(user, value):
    return f"Processed value: {value}"