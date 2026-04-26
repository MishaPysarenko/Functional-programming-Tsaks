def run_pipeline(data, steps):
    for step in steps:
        data = step(data)
    return data

#приклад:
data = range(10)

result = run_pipeline(
    data,
    [
        lambda xs: (x for x in xs if x % 2 == 0),
        lambda xs: (x * x for x in xs)
    ]
)

for x in result:
    print(x)