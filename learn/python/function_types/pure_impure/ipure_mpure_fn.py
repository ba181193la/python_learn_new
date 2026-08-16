
# PURE Funtion ******************************************
def square(num):
    return num * num

print("PURE function:", square(5))  # 25
print("PURE function:", square(5))  # 25

# IMPURE Function

total = 100

def add_money(amount):
    global total
    total += amount
    return total

print("IMPURE function:", add_money(50))  # 150
print("IMPURE function:", add_money(50))  # 200


