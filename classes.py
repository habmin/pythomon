from xmlrpc.client import Boolean
from assets import traits

class Player:
    def __init__(self, name = "Ashy", gender = "Male", nature = traits[0]):
        self.name = name
        self.money = 100
        self.pythomon = []
        # make this have items
        self.bag = []
        self.gender = gender
        # should this be a choice, or just whatever text they want
        # kind mean funny etc was in his notes
        self.nature = nature

class Pythomon:
    def __init__(self, name, max_hp, base_atk, gender, nature, moves, exp_prize = 10):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.base_atk = base_atk
        self.gender = gender
        self.nature = nature
        self.moves = moves
        self.exp = 0
        self.exp_prize = exp_prize
        self.money_prize = 15
        self.status = "alive"

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
    def __init__(self, terrain):
        self.terrain = terrain
        self.player_occupied = False
    
    def __repr__(self) -> str:
        return f"{self.terrain} - Player occupied: {self.player_occupied}"

class Grid:
    def __init__(self):
        pass

class Item:
    def __init__(self, name):
        self.name

class Store:
    def __init__(self):
        self.items = [
            {"name": "Health Spray",
             "price": 20},
            {"name": "Health Drink",
             "price": 50},
            {"name": "Capture Ball",
             "price": 50}
        ]
