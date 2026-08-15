
# without using partial function
def calculate_price(price, gst):
    return price + (price * gst / 100)

print("without partial function:", calculate_price(1000, 18))
print("without partial function:", calculate_price(2000, 18))
print("without partial function:", calculate_price(5000, 18))


# with partial function
from functools import partial

calculate_price_with_gst = partial(calculate_price, gst=18)
print("with partial function:", calculate_price_with_gst(1000))
print("with partial function:", calculate_price_with_gst(2000))
print("with partial function:", calculate_price_with_gst(5000))


def send_message(user, message):
    print(f"Sending '{message}' to {user}")

bala_message = partial(send_message, "Bala")

print("with partial function:")
bala_message("Hello")
bala_message("How are you?")
bala_message("Welcome")