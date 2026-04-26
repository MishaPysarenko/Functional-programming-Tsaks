def middleware(func):
    def wrapper():
        print("Before request")
        result = func()
        print("After request")
        return result
    return wrapper


@middleware
def handle_request():
    return "OK"