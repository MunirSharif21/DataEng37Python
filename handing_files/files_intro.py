# handing files and errors

try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    print("File has not been found")
    # if there is a FileNotFoundError then print this
    print(errmsg)
    # raise
    # above line will cause a noisy crash

print(file, type(file))
orders = file.readlines()
# what if we want our orders without the newline characters
orders = list(map(lambda))
print(orders)
file.close()  # remember to close files!


