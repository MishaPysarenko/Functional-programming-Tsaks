users = [{"name": "Alice", "age": 25}]

result = list(map(lambda u: f"{u['name']} ({u['age']})", users))

print(result)