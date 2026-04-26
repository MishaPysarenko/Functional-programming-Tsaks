from concurrent.futures import ThreadPoolExecutor

transactions = range(1_000_000)

def process(x):
    return x * 2


with ThreadPoolExecutor() as ex:
    mapped = ex.map(process, transactions)

result = sum(mapped)
print(result)