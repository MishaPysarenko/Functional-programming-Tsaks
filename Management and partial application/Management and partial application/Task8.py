def convert(amount, rate):
    return amount * rate

usd_to_uah = partial(convert, rate=40)
eur_to_uah = partial(convert, rate=43)

print(usd_to_uah(100))
print(eur_to_uah(100))
print(usd_to_uah(250))