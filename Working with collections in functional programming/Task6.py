users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 30}
]

names = list(map(lambda u: u["name"], users))
older_30 = list(filter(lambda u: u["age"] > 30, users))
avg_age = sum(map(lambda u: u["age"], users)) / len(users)

print(names)
print(older_30)
print(avg_age)