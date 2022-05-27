""" Create a drink's menu text file
Create a drinks orders text file
Write a function that will take
in a drink order if that order
exists in the menu, write it
to the orders. Otherwise,
raise an error. """

try:
    file = open("drinks_menu")
except FileNotFoundError as errmsg:
    print("File has not been found")
    print(errmsg)

orders = map(lambda line: line.strip("\n"), file)
print(list(orders))
