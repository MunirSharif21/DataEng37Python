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


play = True

while play:
    stop = input("What number would you like to FizzBuzz up to?\n")  # ask stopping number
    fizz_buzz(int(stop) + 1)  # run fizzbuzz game
    answer = input("Would you like to go again? (Y)es/ (N)o\n")  # get response
    if answer.lower() in ("no", "n"):
        play = False
    # if answer isn't "n" then play again...
