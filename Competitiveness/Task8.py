from concurrent.futures import ThreadPoolExecutor

data = range(100)

with ThreadPoolExecutor() as ex:
    squared = list(ex.map(lambda x: x*x, data))

filtered = list(filter(lambda x: x > 100, squared))
result = sum(filtered)

print(result)