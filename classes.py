from random import randint
from assets import traits

class Player:
    def __init__(self, starter, name = "Ashy", gender = "Male", nature = traits[0]):
        self.name = name
        self.money = 100
        self.pythomon = [starter]
        self.bag = ["Health Spray", "Health Spray", "Capture Ball", "Capture Ball", "Capture Ball"]
        self.gender = gender
        self.nature = nature
        self.defeated = False

class Pythomon:
    def __init__(self, pythodeck):
        self.name = pythodeck["name"]
        self.max_hp = pythodeck["hp"]
        self.hp = pythodeck["hp"]
        self.base_atk = pythodeck["base_atk"]
        self.gender = pythodeck["gender"]
        self.nature = traits[randint(0, len(traits) - 1)]
        self.moves = pythodeck["moves"]
        self.exp = 0
        self.exp_prize = pythodeck["exp_prize"]
        self.money_prize = 15
        self.status = "alive"
        self.art = pythodeck["art"]
    
    def level_up(self, exp):
        self.exp += exp
        if exp >= 100:
            self.max_hp += 3
            self.base_atk += 3
            self.hp = self.max_hp
            return True
        return False
        

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
             "price": 50},
            {"name": "Revive",
             "price": 100}
        ]
