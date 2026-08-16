
numbers = [1, 2, 3, 4, 5]

# Normal function:
result = []

for num in numbers:
    result.append(num * 2)

print(result)

# using map function:
result=list(map(lambda xl: xl * 2, numbers))
print("map function",result)

prices = [1000, 2000, 3000]

discount_prices=list(map(lambda pr:pr*0.9, prices))
print("Discount prices",discount_prices)