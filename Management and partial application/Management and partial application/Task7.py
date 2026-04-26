from functools import partial

def add(a, b):
    return a + b

add5 = partial(add, 5)
add10 = partial(add, 10)

print(add5(3))
print(add10(7))