def debug(x):
    print(f"Processing {x}")
    return x


def lazy_map_debug(func, data):
    for x in data:
        yield func(x)


gen = lazy_map_debug(debug, range(5))

for x in gen:
    pass