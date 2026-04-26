def apply_discount(price, percent):
    return price * (1 - percent)

discount_10 = partial(apply_discount, percent=0.1)
discount_20 = partial(apply_discount, percent=0.2)
discount_50 = partial(apply_discount, percent=0.5)

print(discount_10(100), discount_10(250))
print(discount_20(999))