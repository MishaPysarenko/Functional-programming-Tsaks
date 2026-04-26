data = [1,2,3,4,5]

# eager
eager = [x*x for x in data]

# lazy
lazy = (x*x for x in data)

print(type(eager))  # list
print(type(lazy))   # generator

for x in eager:
    print(x)

for x in lazy:
    print(x)