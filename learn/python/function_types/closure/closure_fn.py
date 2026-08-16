# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# # Example usage:
# increment_counter = counter(1)
# print(increment_counter())  # Output: 1
# print(increment_counter())  # Output: 2 

def multiplier(x):
    def multiply(y):
        return x * y

    return multiply


double = multiplier(2)

print(double(5))   # 10
print(double(10))  # 20


def counter(count):
    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# Example usage:
increment_counter = counter(1)
print(increment_counter())  # Output: 1
print(increment_counter())  # Output: 2 

