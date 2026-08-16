def double(x):
    return x * 2

def add_five(x):
    return x + 5

result = add_five(double(10))

print("Function Composition:", result)

def apply_discount(price):
    return price - (price * 10 / 100)

def add_gst(price):
    return price + (price * 18 / 100)

price = 1000

final_price = add_gst(apply_discount(price))

print("Function Composition:", final_price)