def log_request(func):
    def wrapper():
        print("log request")
        return func()
    return wrapper


def authorize(func):
    def wrapper():
        print("authorize")
        return func()
    return wrapper


def handle_errors(func):
    def wrapper():
        try:
            return func()
        except:
            return "error"
    return wrapper


@log_request
@authorize
@handle_errors
def handle_request():
    return "OK"