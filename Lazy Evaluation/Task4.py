def lazy_filter(func, data):
    for x in data:
        if func(x):
            yield x