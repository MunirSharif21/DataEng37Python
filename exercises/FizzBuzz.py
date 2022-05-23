start = 1
stop = 100

fizz = 0
buzz = 0
fizzbuzz = 0

for number in range(start, stop):
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
