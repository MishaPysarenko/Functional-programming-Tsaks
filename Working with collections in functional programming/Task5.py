from functools import reduce

numbers = [1,2,3,4,5,6]

filtered = filter(lambda x: x > 2, numbers)
mapped = map(lambda x: x * 10, filtered)
result = reduce(lambda a,b: a+b, mapped)

print(result)