def curry_add(a):
    return lambda b: a + b

add7 = curry_add(7)
print(add7(5))