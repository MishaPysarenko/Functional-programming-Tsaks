words = ["apple", "banana", "kiwi"]

upper = list(map(str.upper, words))
filtered = list(filter(lambda x: len(x) > 4, words))
total_chars = sum(map(len, words))

print(upper)
print(filtered)
print(total_chars)