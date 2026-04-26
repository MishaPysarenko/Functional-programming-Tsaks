from functools import partial

def add_tax(price, tax):
    return price * (1 + tax)

def apply_discount(price, discount):
    return price * (1 - discount)

def convert_currency(price, rate):
    return price * rate

def add_fee(price, fee):
    return price + fee


tax_20 = partial(add_tax, tax=0.2)
discount_10 = partial(apply_discount, discount=0.1)
usd_to_uah = partial(convert_currency, rate=40)
fee_50 = partial(add_fee, fee=50)


def pipeline(prices):
    result = []
    for p in prices:
        x = discount_10(p)
        x = tax_20(x)
        x = fee_50(x)
        x = usd_to_uah(x)
        result.append(x)
    return result


print(pipeline([100, 250, 400, 999]))