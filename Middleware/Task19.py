def compose_decorators(d1, d2):
    return lambda f: d1(d2(f))