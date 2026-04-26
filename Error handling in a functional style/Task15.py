transactions = [
    {"amount": "100"},
    {"amount": "abc"},
    {"amount": "200"}
]


def parse_amount(t):
    try:
        return Ok(int(t["amount"]))
    except:
        return Error("invalid number")


def positive(x):
    return Ok(x) if x > 0 else Error("not positive")


def sum_results(data):
    total = 0
    for item in data:
        res = parse_amount(item).flat_map(positive)
        if isinstance(res, Ok):
            total += res.value
    return total


print(sum_results(transactions))