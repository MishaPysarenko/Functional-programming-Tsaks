data = range(10**9)

gen = (x for x in data)

for i, x in enumerate(gen):
    if i == 10:
        break
    print(x)