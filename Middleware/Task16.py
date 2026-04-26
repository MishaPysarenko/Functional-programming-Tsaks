def simple_cache(func):
    cache = {}

    def wrapper(x):
        if x in cache:
            return cache[x]
        cache[x] = func(x)
        return cache[x]

    return wrapper


@simple_cache
def square(x):
    print("Calculating...")
    return x * x