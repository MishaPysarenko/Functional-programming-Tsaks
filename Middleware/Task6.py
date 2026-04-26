def debug_args(func):
    def wrapper(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@debug_args
def greet(name, prefix="Hello"):
    return f"{prefix}, {name}"