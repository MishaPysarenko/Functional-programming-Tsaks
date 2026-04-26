import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time:", end - start)
        return result
    return wrapper


@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


slow_sum(100000)