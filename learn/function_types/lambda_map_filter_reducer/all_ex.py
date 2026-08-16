
prices = [1000, 2000, 5000, 10000, 20000]

# 10% discount:
discounted = list(
    map(lambda price: price * 0.9, prices)
)

print("Map",discounted)

# ₹5,000 or more products:

filtered = list(
    filter(lambda price: price >= 5000, discounted)
)

print("Filter",filtered)


from functools import reduce

total = reduce(
    lambda a, b: a + b,
    filtered
)

print("Reduce",total)