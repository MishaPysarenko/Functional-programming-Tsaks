from concurrent.futures import ThreadPoolExecutor

def risky(x):
    if x == 0:
        raise ValueError
    return 10 / x


def safe(func):
    def wrapper(x):
        try:
            return func(x)
        except:
            return None
    return wrapper


def safe_parallel_map(func, data):
    with ThreadPoolExecutor() as ex:
        return list(ex.map(safe(func), data))