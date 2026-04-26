def debug(x):
    print("DEBUG:", x)
    return x


data = (debug(x) for x in range(5))

for x in data:
    pass