# L-E_G-B


# local variable 


food = "burger"
def order():
    food ="pizza"
    return food

print("local variable:",order())

# global variable

def print_food():
    print("global variable:",food)

print_food()

# enclosing function

def outer():
    food = "pasta"
    def inner():
        print("enclosing function:",food)
    inner()
outer()

# built-in variable
print("built-in variable:",len("hello world"))
print("built-in variable:",max(1,2,3,4,5))
print(__file__)


