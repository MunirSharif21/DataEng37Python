# Pillars of OOP:
# Abstraction
# Encapsulation (keep certain stuff hidden away, keep methods hidden)
# Inheritance (use what is already there)
# Polymorphism ("Many-Forms") (inheritance but and extend on what you inherit)

# HOMEWORK - Create your own classes to demonstrate these pillars

# SOLID Principles:
# Single-responsibility
# Open-closed (open for extension, closed for modification)
# Liskovs Substitution
# Interface Segregation
# Dependency Inversion

class Pokemon:
    def __init__(self, name, type, hp, attack, defence):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.lvl = 1
        self.moves = []

    def recieve_attack(self, power, is_super_effective=False):
        if is_super_effective:
            self.hp -= (power - self.defense) * 1.5
        else:
            self.hp -= (power- self.defense)

    def lvl_up(self, levels=1):
        self.lvl += levels
        self.hp += levels * 2
        self.attack += levels
        self.defense += levels
