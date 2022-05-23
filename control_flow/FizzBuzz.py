def fizz_buzz(stop):

    fizz = 0
    buzz = 0
    fizzbuzz = 0

    for number in range(1, stop):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            fizzbuzz += 1
        elif number % 5 == 0:
            print("Buzz")
            buzz += 1
        elif number % 3 == 0:
            print("Fizz")
            fizz += 1
        else:
            print(number)

    print(f'\nFizz: {fizz}\nBuzz: {buzz}\nFizzBuzz: {fizzbuzz}')


keep_asking = True
while keep_asking:  # while True...
    stop = input("What number would you like to FizzBuzz up to?\n")
    if stop.isdigit():  # if the input was a number...
        fizz_buzz(int(stop) + 1)  # add 1 so fizzbuzz goes up to that number inclusive
        keep_asking = False  # stop asking for a number if it's an int
    else:
        print("Please enter a valid number in digits.")
