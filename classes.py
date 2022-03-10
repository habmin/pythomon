from random import randint
from assets import traits
from assets import pythodeck

class Player:
    def __init__(self, starter, trophy, name = "Ashy", gender = "Male", nature = traits[0]):
        self.name = name
        self.money = 100
        self.pythomon = [starter]
        self.bag = ["Health Spray", "Health Spray", "Capture Ball"]
        self.gender = gender
        self.nature = nature
        self.defeated = False
        self.trophies = [trophy]

    def check_defeated(self):
        for pytho in self.pythomon:
            if pytho.status == "alive":
                return False
        self.defeated = True
        return True

    def buy(self, item):
        if self.money < item["price"]:
            return False
        else:
            self.bag.append(item["name"])
            self.money -= item["price"]
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
        if self.exp >= 100:
            self.max_hp += 3
            self.base_atk += 3
            if self.status == "alive":
                self.hp = self.max_hp
                self.healthbar = "████████████████████"
            self.exp -= 100
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
    
    def heal(self, hp_amount):
        self.hp = min(self.max_hp, self.hp + hp_amount)
        self.healthbar = ("█" * int(((self.hp / self.max_hp) * 20))) + ("░" * (20 - int(((self.hp / self.max_hp) * 20))))
    
    def revive(self):
        self.status = "alive"
        self.hp = self.max_hp // 2
        self.healthbar = ("█" * int(((self.hp / self.max_hp) * 20))) + ("░" * (20 - int(((self.hp / self.max_hp) * 20))))
        
class Trainer:
    def __init__(self, name, pythomon, money, prize, about):
        self.name = name    
        self.pythomon = pythomon
        self.money = money
        self.prize = prize
        self.about = about

class Square:
    def __init__(self, terrain):
        self.terrain = terrain
        self.player_occupied = False
    
    def __repr__(self) -> str:
        return f"{self.terrain} - Player occupied: {self.player_occupied}"

class Store:
    def __init__(self):
        self.items = [
            {"name": "Health Spray",
             "price": 30},
            {"name": "Health Drink",
             "price": 60},
            {"name": "Revive",
             "price": 100},
            {"name": "Capture Ball",
             "price": 60}
        ]
