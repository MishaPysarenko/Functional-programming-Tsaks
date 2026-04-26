def greater_than(limit):
    def inner(value):
        return value > limit
    return inner


greater_than_10 = greater_than(10)
greater_than_100 = greater_than(100)

numbers = [5, 10, 15, 50, 100, 150]

print(list(filter(greater_than_10, numbers)))
print(list(filter(greater_than_100, numbers)))