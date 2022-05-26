""" Create a Budget class that can keep track of different budget
categories like food, clothing, and entertainment. These should
allow for depositing and withdrawing funds from each category,
as well computing category balances and transferring balance
amounts between categories. """


class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = 0
        self.clothing = 0
        self.entertainment = 0

    def deposit(self, category, amount):
        self.category += amount

    def withdraw(self, category, amount):
        pass

