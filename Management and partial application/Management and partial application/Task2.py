def discount(price, percent):
    return price * (1 - percent)

def convert(amount, rate):
    return amount * rate

def greet(greeting, name):
    return f"{greeting}, {name}!"

discount_10 = lambda price: discount(price, 0.1)
convert_usd = lambda amount: convert(amount, 40)
hello = lambda name: greet("Hello", name)