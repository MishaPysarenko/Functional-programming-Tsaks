from functools import reduce

orders = [
    {"id": 1, "items": [100, 200]},
    {"id": 2, "items": [50, 50, 50]},
]

order_sums = list(map(lambda o: sum(o["items"]), orders))
total_sum = sum(order_sums)
max_order = max(order_sums)

print(order_sums)
print(total_sum)
print(max_order)