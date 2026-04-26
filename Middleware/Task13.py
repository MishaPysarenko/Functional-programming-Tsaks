def logger(func):
    def wrapper(*args, **kwargs):
        print("log")
        return func(*args, **kwargs)
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def positive_only(func):
    def wrapper(*args):
        if any(a < 0 for a in args):
            return "error"
        return func(*args)
    return wrapper


@logger
@timer
@positive_only
def process_data(x):
    return x * 2