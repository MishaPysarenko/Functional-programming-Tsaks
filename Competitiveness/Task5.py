from concurrent.futures import ThreadPoolExecutor

def parallel_map(func, data):
    with ThreadPoolExecutor() as ex:
        return list(ex.map(func, data))