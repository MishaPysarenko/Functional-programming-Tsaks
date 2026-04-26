import time
from concurrent.futures import ThreadPoolExecutor

data = range(1_000_000)

# sequential
start = time.time()
list(map(lambda x: x*x, data))
print("seq:", time.time() - start)

# parallel
start = time.time()
with ThreadPoolExecutor() as ex:
    list(ex.map(lambda x: x*x, data))
print("parallel:", time.time() - start)