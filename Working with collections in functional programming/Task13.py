from functools import reduce

def run_pipeline(data, steps):
    return reduce(lambda acc, f: f(acc), steps, data)


transactions = [
    {"currency": "USD", "amount": 100},
    {"currency": "EUR", "amount": 200}
]

def filter_usd(data):
    return list(filter(lambda x: x["currency"] == "USD", data))

def convert_to_uah(data):
    return list(map(lambda x: x["amount"] * 40, data))

def sum_all(data):
    return sum(data)


result = run_pipeline(
    transactions,
    [filter_usd, convert_to_uah, sum_all]
)

print(result)