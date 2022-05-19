a = 1  # int
b = 2  # int
c = 3.5  # float
d = "Hello!"  # str

print(a)
print(b)
print(c)
print(d)

# Python is a dynamically typed language meaning you don't have to state the data type for a variable

print(type(a))  # I used CTRL+D to copy this line
print(type(b))
print(type(c))
print(type(d))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

b = 100

print(a + b)
total = b + c
print(total)

'''
What happens when you combine ints
and floats with different
arithmetic operators?
'''

print(5 + 3.2)
print(5 + 5.0)  # answer is float
print(5 + 5)

print(21 % 9)  # modulo
