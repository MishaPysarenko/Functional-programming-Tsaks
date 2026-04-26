def safe_divide(a, b):
    if b == 0:
        return Error("division by zero")
    return Ok(a / b)