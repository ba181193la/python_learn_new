try:
    numers_of_items = int(input("enetr items: "))
    total = numers_of_items * 2
    avr = total /numers_of_items
    print("total",total)
    print("avr",avr)
except ZeroDivisionError:
    print("you cannot order the 0 itme")
except FileNotFoundError:
    print("-FileNotFoundError-you cannot order the 0 itme")
finally:
    print("finally logout")

print("hello run the code")


# numers_of_items = int(input("enetr items: "))
# total = numers_of_items * 2
# avr = total / numers_of_items
# print("total", total)
# print("avr", avr)
# print("hello run the code")
