class Player:
    def __init__(self, name, gender):
        self.name = name
        self.money = 100
        # make this have items
        self.bag = []
        self.gender = gender
        # should this be a choice, or just whatever text they want
        # kind mean funny etc was in his notes
        self.nature = []

class Pythomon:
    def __init__(self, name, hp, base_atk, gender, nature, moves):
        self.name = name
        self.hp = hp
        self.base_atk = base_atk
        self.gender = gender
        self.nature = nature
        self.moves = moves

class Trainer:
    def __init__(self, name, pythomon, money, prize, about, flair):
        self.name = name
        self.pythomon = pythomon
        self.money = money
        self.prize = prize
        self.about = about
        # should be a dict of sayings/taunts when they win, lose
        self.flair = flair

class Square:
    def __init__(self):
        pass

class Grid:
    def __init__(self):
        pass

store = [
    {"Health Spray": 20},
    {"Health Drink": 50},
    {"Capture Ball": 50}
]
