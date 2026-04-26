def read_lines():
    yield "line 1"
    yield "line 2"
    yield "line 3"


for line in read_lines():
    print(line)