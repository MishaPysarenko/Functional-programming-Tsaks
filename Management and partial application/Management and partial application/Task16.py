from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)  # partial

def multiply_curried(a):
    return lambda b: a * b       # currying

def add(a, b):
    return a + b                 # neither