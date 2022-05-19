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
"""
x = None
print(x is None)
