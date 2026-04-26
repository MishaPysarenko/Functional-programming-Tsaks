def safe_divide(a, b):
    if b == 0:
        return ("error", "division by zero")
    return ("ok", a / b)