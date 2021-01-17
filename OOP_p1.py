class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy', 44)
print(f"The player: {player1.name} is {player1.age} years old")