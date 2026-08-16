
numbers = [1, 2, 3, 4, 5, 6]

# Normal function:
def is_even(num):
    return num % 2 == 0

# Using filter function:
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

# using lambda function with filter:
result=list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (using lambda):", result)


products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 1000},
    {"name": "Monitor", "price": 15000}
]

expensive = list(
    filter(lambda product: product["price"] > 10000, products)
)

print(expensive)