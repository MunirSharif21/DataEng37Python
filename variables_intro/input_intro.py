"""
name = input("What is your name?\n")
age = input("What is your age?\n")
height_cm = input("How tall are you in cm?\n")
print(f"Hello {name}, you are {age * 2} years old and {height_cm}cm tall.")

t = True
f = False
print(t, type(t))

print(True and True)
print(True and False)
print(False and True)
print(False and False)

text = "Hello World!"
print(text.isalpha())  # check if ALL CHARACTERS are letters (space in string will return false)
print(text.isupper())  # check if ALL LETTERS are uppercase
print(text.islower())  # check if ALL LETTERS are lowercase
print(text.endswith("!"))  # check if string ends with specified value
print(text.startswith("H"))  # check if string begins with specified value

x = None
print(x is None)
"""

shopping_list = ["Bread", "Bananas", "Biscuits", "Oat Milk"]
print(shopping_list, type(shopping_list))

# INDEXING AND SLICING

print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[::-1])

# Lists ARE MUTABLE

shopping_list[0] = "Sugar"
print(shopping_list)
shopping_list.append("Milk")
print(len(shopping_list))
shopping_list.remove("Bananas")
# only the first instance of bananas will be removed
# if there are multiple bananas in the list

hi = "Hello"
print(hi.upper())
print(hi)
# upper method only returns something
# the original string won't be changed

print(shopping_list.pop())
# removes item from list and gives it you
# by default, last item will be removed
# unless you provide an index.
print(shopping_list)

mixed_list = [1, 2, 3.0, 4+5j, "greetings", True, False, None]
print(mixed_list)

nested_list = [[1, 2], [3, 4]]
print(nested_list[1][-1])  # second list, last item (4)
