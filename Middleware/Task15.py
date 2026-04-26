def limit_calls(n):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= n:
                return "Call limit exceeded"
            count += 1
            return func(*args, **kwargs)

        return wrapper
    return decorator


@limit_calls(3)
def ping():
    return "pong"