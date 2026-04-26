def safe_divide(a, b):
    if b == 0:
        return Error("division by zero")
    return Ok(a / b)


def safe_pipeline(x):
    return (
        safe_divide(x, 2)
        .map(lambda x: x + 10)
        .flat_map(lambda x: safe_divide(x, 0))
    )