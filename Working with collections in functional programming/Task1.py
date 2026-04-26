numbers = [1, 2, 3, 4, 5]

# lambda
print(list(map(lambda x: x * x, numbers)))
print(list(map(lambda x: x * 2, numbers)))
print(list(map(lambda x: str(x), numbers)))

# named functions
def square(x): return x * x
def double(x): return x * 2
def to_str(x): return str(x)

print(list(map(square, numbers)))
print(list(map(double, numbers)))
print(list(map(to_str, numbers)))