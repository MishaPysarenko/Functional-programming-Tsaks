def lazy_map(func, data):
    for x in data:
        yield func(x)