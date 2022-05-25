class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old dog"
        else:
            return self.__str__()
            # return f"A {self.age} years old dog"


fido = Dog(5)
print(f"Fido is {fido}")
print(f"Fido is {fido:dog}")
