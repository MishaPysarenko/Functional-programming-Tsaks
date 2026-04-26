import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(x):
    time.sleep(1)
    return x


data = range(10)

# sequential
start = time.time()
list(map(fetch_data, data))
print("seq:", time.time() - start)

# parallel
start = time.time()
with ThreadPoolExecutor() as ex:
    list(ex.map(fetch_data, data))
print("parallel:", time.time() - start)