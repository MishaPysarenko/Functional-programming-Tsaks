def safe_divide(a, b):
    if b == 0:
        return Nothing()
    return Some(a / b)