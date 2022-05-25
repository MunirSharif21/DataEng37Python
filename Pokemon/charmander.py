from pokemon import Pokemon
from move import Move
# Charmander imports the Pokemon module from the pokemon.py class


class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
            name="Charmander",
            type="Fire",
            hp=7,
            attack=9,
            defence=5
        )
        self.moves.append(Move("Scratch", "Normal", 10))
        self.moves.append(Move("Growl", "Normal", 0))

    def Pikachu(Pokemon):
        def __init__(self):
            super().__init__(
                name="Pikachu",
                type="Electric",
                hp=6,
                attack=6,
                defence=6
            )
            self.moves.append(Move("Thundershock", "Electric", 20))
            self.moves.append(Move("Tail Whip", "Normal", 0))

    def use_move(self, move_name) -> (int, str):
        for move in self.moves:
            if move_name == move_name:
                print(f"{self.name} used {move.name}")
                return move.power + self.attack, move.type


char = Charmander()

result = char.use_move("Scratch")
print(result, type(result))

power, move_type = char.use_move("Growl")
print(power, type(power))

print(move_type, type(move_type))