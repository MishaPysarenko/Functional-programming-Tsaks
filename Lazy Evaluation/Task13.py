transactions = range(1_000_000)

filtered = (x for x in transactions if x % 2 == 0)
mapped = (x * 10 for x in filtered)

result = 0
for i, x in enumerate(mapped):
    if i == 100:
        break
    result += x

print(result)