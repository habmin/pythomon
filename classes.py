from random import randint
from assets import traits
from assets import pythodeck

class Player:
    def __init__(self, starter, name = "Ashy", gender = "Male", nature = traits[0]):
        self.name = name
        self.money = 100
        self.pythomon = [starter]
        self.bag = ["Health Spray", "Health Spray", "Capture Ball", "Capture Ball", "Capture Ball"]
        self.gender = gender
        self.nature = nature
        self.defeated = False
        # self.pythomon.append(Pythomon(pythodeck[1]))
        # self.pythomon.append(Pythomon(pythodeck[2]))
        # self.pythomon.append(Pythomon(pythodeck[3]))
        # self.pythomon.append(Pythomon(pythodeck[4]))
        # self.pythomon.append(Pythomon(pythodeck[5]))
        # self.pythomon.append(Pythomon(pythodeck[6]))
    
    def check_defeated(self):
        for pytho in self.pythomon:
            if pytho.status == "alive":
                return False
        return True

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
        self.money_prize = 20
        self.status = "alive"
        self.art = pythodeck["art"]
        self.healthbar = "████████████████████"

    def level_up(self, exp):
        self.exp += exp
        if exp >= 100:
            self.max_hp += 3
            self.base_atk += 3
            if self.status == "alive":
                self.hp = self.max_hp
                self.healthbar = "████████████████████"
            self.exp = 100 - self.exp
            return True
        return False
    
    def attack(self, target, move_selection):
        target.hp -= self.base_atk + self.moves[move_selection]["power"]
        target.healthbar = ("█" * int(((target.hp / target.max_hp) * 20))) + ("░" * (20 - int(((target.hp / target.max_hp) * 20))))
        if target.hp <= 0:
            target.hp = 0
            target.healthbar = "░░░░░░░░░░░░░░░░░░░░"
            target.status = "dead"
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
