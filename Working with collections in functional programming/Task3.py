from functools import reduce

numbers = [1,2,3,4,5]

print(reduce(lambda a,b: a+b, numbers))      # sum
print(reduce(lambda a,b: a*b, numbers))      # product
print(reduce(lambda a,b: a if a>b else b, numbers))  # max
print(reduce(lambda a,b: a if a<b else b, numbers))  # min