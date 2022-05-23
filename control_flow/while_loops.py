x = 0
while x < 10:
    print(f"While loop running {x}")
    x += 1  # x = x + 1
    if x == 5:
        print("Yay, 5!")
        break
print("While loop finished")
