sales = [100, 200, 300, 400]

discounted = list(map(lambda x: x * 0.9, sales))
avg = sum(discounted) / len(discounted)
max_sale = max(discounted)

print(discounted)
print(avg)
print(max_sale)