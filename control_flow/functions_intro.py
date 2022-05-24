# print()
# input()
# type()
#
# DRY - DON'T REPEAT YOURSELF
#
# Function Definition
# def greeting(name):
#     print(f"Hello, {name}.")
#
#
# Call to Function
# greeting("Konrad")
# greeting("Harry")
# greeting("Dan")
#
#
# Functions either do or return something...
#
# def advanced():
#     yield "Something"  # does something without finishing function
#     return "Hey"
#
#
# def greeting_advanced(name = "... you!"):
#     return "Hello" + name
#
#
# greeting_advanced()
#
# print("one", "two", 6345, {})


# def multiargs(*args):
#     print(args, type(args))
#
#
# multiargs(1, 2, 3)


def product(num1, *nums):  # have to call function with at least one number...
    # if not nums:
    #     return None
    result = 1
    for num in nums:
        result *= num
    return result


print(product(1, 2, 3))
print(product())
