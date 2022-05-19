h = "Hello world!"

double = "Double Quotes"
single = 'Single Quotes'

print(double, single)

# failure = "I said " Oh no!""
double_in_single = 'I said "Oh no!"'
both = 'I said "Oh No! He\'s in trouble"'
print(both)

string_block = """
Everything in here
is part of the string

Up until
The Last 3 quotes
"""
print(string_block)

# STRING INDEXING AND SLICING

print(h[1])  # remember that python indexes begin at 0
print(h[-1])  # print last character in string

print(h[2:7])  # inclusive, it will go up to 7 but not include

print(h[3:8])
print(h[3:-4])

print(h[:-4])
print(h[3:])
print(h[1:-3:3])  # return every third character
print(h[4::2])  # return h[4] to end of string in twos
print(h[::-1])  # reverse a string

# Methods

print(type(h))
print(h.lower())

"""
str.strip()
Return a copy of the string with the leading
and trailing characters removed. The chars 
argument is a string specifying the set of
characters to be removed. If omitted or
None, the chars argument defaults to removing
whitespace.

str.count()
Return the number of non-overlapping occurrences
of substring sub in the range [start, end].
Optional arguments start and end are interpreted
as in slice notation.

str.upper()
Return a copy of the string with all the cased
characters 4 converted to uppercase.

str.capitalize
Return a copy of the string with its first
character capitalized and the rest lowercased.

str.replace()
Return a copy of the string with all occurrences
of substring old replaced by new. If the optional
argument count is given, only the first count
occurrences are replaced.
"""

# F-String (Formatted)
name = "Lassie"
years = 7
height_cm = 60.2
print(f"{name} is {years * 7} years old in dog years and {height_cm:.2f}cm tall")

score = 16
max_score = 26
print(f"You scored {score/max_score:.2%}")
