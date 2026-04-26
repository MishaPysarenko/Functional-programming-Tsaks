from functools import reduce

data = [[1,2], [3,4], [5]]

flat = reduce(lambda a,b: a + b, data)
print(flat)