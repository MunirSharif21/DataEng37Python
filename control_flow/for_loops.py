alphabet = ["A", "B", "C", "D", "E"]

for letter in alphabet:
    print(f'{letter} {alphabet.index(letter)}')
    if letter == "E":
        print("END")

nest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for sublist in nest:
    print(sublist)
    for number in sublist:
        print(number)

hi = "Hello World!"

print(hi)
for c in hi:
    print(c)

myDictionary = {
    "key": "value",
    "another_key": ["another_value", "third_value"],
    "hello": {
        "firstname": "Munir",
        "lastname": "Sharif"
    }
}

for k in myDictionary:
    print(k)

for v in myDictionary:
    print(v)

# unpacking a tuple
t = (10, 50)
a, b = t
print(a)
print(b)

for i in range(0, 3): # could also just put 3 as it begins from 0 by default
    print(i)
