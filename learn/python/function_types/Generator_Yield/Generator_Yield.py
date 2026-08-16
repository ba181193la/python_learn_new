
def get_numbers():
    return [1, 2, 3, 4, 5]

numbers = get_numbers()

print(numbers)

# yeild
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 1000},
    {"id": 3, "name": "Keyboard", "price": 2000},
    {"id": 4, "name": "Monitor", "price": 15000}
]

# Now our generator:
def get_products(products):
    for product in products:
        yield product

def get_products(products):
    for product in products:
        yield product

product_generator = get_products(products)

for product in product_generator:
    print(product)