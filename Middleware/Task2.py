def greet(name):
    return f"Hello, {name}"


def wrapper(func):
    def inner(name):
        print("Before function call")
        result = func(name)
        print("After function call")
        return result
    return inner


wrapped = wrapper(greet)
print(wrapped("Alice"))