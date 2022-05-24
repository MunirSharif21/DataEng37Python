class Dog:
    # animal_type = "canine"  # class variable

    def __init__(self, dog_name, colour):  # initialise
        self.animal_type = "canine"
        self.legs = 4
        self.name = dog_name
        self.colour = colour

    def bark(self):  # method. self means referring to current class
        return f"Woof! I am a {self.animal_type}."


fido = Dog("Fido", "Black")  # instantiation = creating an INSTANCE of the class
print(fido.animal_type)
print(fido.bark())
print(fido.name)
print(fido.colour)

print(fido)
print(type(fido))

# this won't work after the __init__ part was written
Dog.animal_type = "feline"
print(fido.animal_type)
print(fido.bark())
