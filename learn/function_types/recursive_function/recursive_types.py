def count_down(n):
    if n == 0:
        return

    print(n)
    count_down(n - 1)

count_down(5)

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))