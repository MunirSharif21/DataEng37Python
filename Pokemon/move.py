class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power


flamethrower = Move(
    name="Flamethrower",
    type="Fire",
    power=100
)

print(flamethrower)
print(type(flamethrower))
print(flamethrower.power)
