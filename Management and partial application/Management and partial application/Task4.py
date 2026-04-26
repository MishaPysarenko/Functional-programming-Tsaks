def multiply_curried(a):
    def inner(b):
        return a * b
    return inner


double = multiply_curried(2)
triple = multiply_curried(3)

nums = [1,2,3,4,5]

print([double(x) for x in nums])
print([triple(x) for x in nums])