def lazy_reduce(func, data, initial):
    acc = initial
    for x in data:
        acc = func(acc, x)
        yield acc