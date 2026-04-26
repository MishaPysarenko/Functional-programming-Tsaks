import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def heavy_task(x):
    total = 0
    for i in range(10_000_000):
        total += i * x
    return total


data = [1,2,3,4]

# sequential
start = time.time()
list(map(heavy_task, data))
print("seq:", time.time() - start)

# threads
start = time.time()
with ThreadPoolExecutor() as ex:
    list(ex.map(heavy_task, data))
print("threads:", time.time() - start)

# processes
start = time.time()
with ProcessPoolExecutor() as ex:
    list(ex.map(heavy_task, data))
print("processes:", time.time() - start)