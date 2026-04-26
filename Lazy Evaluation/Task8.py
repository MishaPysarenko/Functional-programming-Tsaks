data = range(1, 1000000)

result = pipeline(
    data,
    [
        lambda xs: lazy_filter(lambda x: x % 2 == 0, xs),
        lambda xs: lazy_map(lambda x: x*x, xs)
    ]
)

for i, x in enumerate(result):
    if i == 5:
        break
    print(x)