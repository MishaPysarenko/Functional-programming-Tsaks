def power(base):
    def inner(exp):
        return base ** exp
    return inner


from functools import partial

def power_fn(base, exp):
    return base ** exp

square = partial(power_fn, exp=2)
cube = partial(power_fn, exp=3)

print(square(5))
print(cube(3))