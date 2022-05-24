print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


def divisors(number, end=101):
    mylist = []
    for i in range(1, end):
        if number % i == 0:
            mylist.append(i)
    return mylist


print(divisors(21))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


def myfunction(num1, num2):
    list1 = divisors(num1)
    list2 = divisors(num2)
    if num1 in list2:
        return True
    elif num2 in list1:
        return True
    else:
        return False


print(myfunction(21, 12))
print(myfunction(5, 10))

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


def question2a(letter):
    print(alphabet.index(letter.lower()))


question2a("M")


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

name = "Munir"
mystring = ""
for char in name.lower():
    mystring += str(alphabet.index(char))
print(mystring)

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


def password(string):
    sum = 0
    for num in string:
        sum += int(num)
    return int(string) - sum


print(password(mystring))

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


def is_prime(number):
    factors = divisors(number)
    if len(factors) == 2:
        return True  # A prime number should only have two factors (itself and 1)
    return False  # if the length of factors is greater than 2 then it's not a prime


print(is_prime(13))  # True
print(is_prime(21))  # False
print(is_prime(7))   # True

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


def finish_this(number):
    if isinstance(number, int):  # check if variable is an integer
        if len(divisors(number)) > 2:
            return False
        return True
    return None


print(finish_this("Text"))  # Return None
print(finish_this(13))  # True
print(finish_this(21))  # False
