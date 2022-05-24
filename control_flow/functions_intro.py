# print()
# input()
# type()

# DRY - DON'T REPEAT YOURSELF

# Function Definition
# def greeting(name):
#     print(f"Hello, {name}.")
#
#
# Call to Function
# greeting("Konrad")
# greeting("Harry")
# greeting("Dan")

# Functions either do or return something...

# def advanced():
#     yield "Something"  # does something without finishing function
#     return "Hey"


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


# def product(num1, *nums):  # have to call function with at least one number...
#     # if not nums:
#     #     return None
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
#
# print(product(1, 2, 3))
# print(product())  # if function is called with no arguments, return None.


# def kwargs_demo(**kwargs):
#     print(kwargs, type(kwargs))
#
#
# print(kwargs_demo(a="One", b="Two"))

# def calculate_tip(list_of_meals, total_cost, tip_pc):
# """Prints a list of meals followed by info on total with and without tip."""  # DOCSTRING
#     print("You had: ")
#     for meal in list_of_meals:
#         print(f" - {meal}")
#     print(f"Your total is: £{total_cost:.2f}")
#     print(f"With a {tip_pc:.0%} tip, the total is £{total_cost * (1 + tip_pc):.2f}")
#
#
# calculate_tip(["Burger", "Pizza"], 18.50, 0.1)
# calculate_tip(
#     list_of_meals=["Hot Dog", "French Fries"],
#     tip_pc=0.15,
#     total_cost=24
# )


# def calculate_total_cost(**meal_prices):
#     """
#     total = 0
#     for meal in meal_prices:
#         total += meal_prices[meal]
#     return(f"Your total is: £{total:.2f}")
#     """
#     return sum(meal_prices.values())  # above code works but this is simple
#
#
# print(calculate_total_cost(
#     Pizza=8.50,
#     Burger=9.00,
#     HotDog=9.20
#     )
# )


# def greeting(name: str):  # add a hint so your IDE will tell you to use a string here
#     print("Hello" + name)
#
#
# greeting()


# def division(denom: int, num: int) -> float:  # this function will return a float
#     return denom / num
#
#
# a = division(12, 6)  # now when i do "a." in the IDE, all the options will be for floats


# Good Functions
# - Name them clearly, lowercase_with_underscores
# - Clear argument names
# - Functions that don't RETURN something, return None
# - Keep them small
# - Use comments
# - Consider type hints

def fizzbuzz_line(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)


def fizzbuzz_game():
    for i in range(1, 101):
        print(fizzbuzz_line(i))


fizzbuzz_game()
