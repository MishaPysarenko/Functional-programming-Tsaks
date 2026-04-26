from concurrent.futures import ThreadPoolExecutor

data = [1,2,3,4,5]

with ThreadPoolExecutor() as ex:
    result = list(ex.map(lambda x: x*x, data))

print(result)