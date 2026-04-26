def add_curried(a):
    def inner(b):
        return a + b
    return inner


print(add_curried(2)(3))
print(add_curried(10)(5))

add10 = add_curried(10)
print(add10(7))
print(add10(100))