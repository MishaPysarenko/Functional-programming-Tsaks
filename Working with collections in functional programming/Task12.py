products = [
    {"name": "A", "price": 100},
    {"name": "B", "price": 200},
    {"name": "C", "price": 300}
]

discounted = list(map(lambda p: {"name": p["name"], "price": p["price"] * 0.8}, products))
filtered = list(filter(lambda p: p["price"] > 150, discounted))
names = list(map(lambda p: p["name"], filtered))

print(discounted)
print(names)