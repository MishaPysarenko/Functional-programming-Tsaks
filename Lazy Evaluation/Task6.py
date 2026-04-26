data = range(1, 10)

result = lazy_map(
    lambda x: x*x,
    lazy_filter(lambda x: x % 2 == 0, data)
)

for x in result:
    print(x)