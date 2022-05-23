x = 0
while x < 10:
    print(f"While loop running {x}")
    x += 1  # x = x + 1
    if x == 5:
        print("Yay, 5!")
        break
print("While loop finished")

keep_asking = True
age_int = None

while keep_asking:
    age = input("What is your age?\n")
    if age.isdigit():
        age_int = int(age)
        keep_asking = False
    else:
        print("Please enter a valid number in digits.")
print(f"Your age is {age_int}")
