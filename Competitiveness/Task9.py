def pipeline(data, steps):
    for step in steps:
        data = step(data)
    return data