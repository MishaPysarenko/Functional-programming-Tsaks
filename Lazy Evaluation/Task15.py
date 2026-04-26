def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1


gen = infinite_numbers()

print(next(gen))
print(next(gen))
print(next(gen))