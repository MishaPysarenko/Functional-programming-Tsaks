def log_with_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"[{prefix}] {result}")
            return result
        return wrapper
    return decorator


@log_with_prefix("INFO")
def run_task():
    return "Done"