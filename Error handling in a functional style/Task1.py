def divide(a, b):
    return a / b

#try/except версія
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None