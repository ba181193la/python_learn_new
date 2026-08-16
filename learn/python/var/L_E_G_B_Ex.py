
delivey_app="zomatto"

def hotel():
    food="pitza"
    def order_now():
        qty=2
        print(f"ordering {qty} {food} using {delivey_app}")
    order_now()
hotel()

print(__file__)
     