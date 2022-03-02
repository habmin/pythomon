traits = ["Cheerful", "Serious", "Determined", 
          "Chaotic", "Cool-Headed", "Aggressive", 
          "Polite", "Naughty", "Smart", "Polemic", 
          "Lazy", "Shady", "Sleepy"]

pythodeck = [  
    # 0-3 are the starter pythomon
    {
        "name": "Pecan Chew", 
        "hp": 100,
        "base_atk": 7,
        "gender": "rat",
        "moves": {
            "name": "Electro",
            "power": 20},
        "exp_prize": 50,
        "art": [
            "    ▒▒         ▒▒ ",
            "      ▒▒▒▒▒▒▒▒▒   ",
            " ▒▒▒▒  ▒▓▒▒▒▓▒    ",
            "    ▒▒▒▓▒▒▓▒▒▓    ",
            "    ▒▒ ▒▒▒▒▒▒▒    ",
            "     ▒▒▒▒▒▒▒▒▒▒   ",
            "       ▒▒▒▒▒▒▒    ",
            "       ▒▒   ▒▒    ",
        ]},
    {
        "name": "Charm Dander", 
        "hp": 70,
        "base_atk": 13,
        "gender": "fire boi",
        "moves": {
            "name": "Fire",
            "power": 20},
        "exp_prize": 50,
        "art": [
            "         ▒▓▓▓▓▒   ",
            "         ▓▓▒▓▓▒▒  ",
            " ▒▓▒  ▒  ▓▓▓▓▓▓▒▒ ",
            " ▓▒   ▒▓▓▓▒▒▒▒▓▓  ",
            " ▒▒    ▒▓▒▒▒▒▒▒   ",
            "  ▒    ▓▓▒▒▒▒▒    ",
            "   ▒▓▓▓▓▓▒▒▒▒▓▒   ",
            "       ▓▓▓  ▓▓▓   "
        ]},
    {
        "name": "Bowl Bar Sore", 
        "hp": 120,
        "base_atk": 5,
        "gender": "pretty flower",
        "moves": {
            "name": "Flower",
            "power": 20},
        "exp_prize": 50,
        "art": [
            "  ▒▒▒▒▒           ",
            " ▒▒▒▒▒▒▒▒▒▒       ",
            "█▓▒▒▒▒▒▓█▓▓       ",
            "▓██▓▓▓▒▒▒▒█▓▒▒▒   ",
            " ▒▓██▓▒▒▒▒▒▒▒▒▓▒  ",
            " ▒▓▒▒▒▒▒▒▒▓▒▒▒▒▓▓ ",
            " ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒ ",
            " ▓   ▓▓▒▓▒▒       ",
        ]},
    {
        "name": "Squirt Turtle", 
        "hp": 85,
        "base_atk": 10,
        "gender": "glasses-wearer",
        "moves": {
            "name": "Water Gun",
            "power": 20},
        "exp_prize": 50,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},

    # 4-23 are selected at random
    {
        "name": "Zoo Hat", 
        "hp": 50, 
        "base_atk": 5,
        "gender": "flying rat",
        "moves": {
            "name": "SCREAMING",
            "power": 10},
        "exp_prize": 15,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Go Dean", 
        "hp": 60, 
        "base_atk": 7, 
        "gender": "pretty fish",
        "moves": {
            "name": "Splash",
            "power": 10},
        "exp_prize": 15,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Met a Pod", 
        "hp": 70, 
        "base_atk": 0, 
        "gender": "facebook lover",
        "moves": {
            "name": "Hard Mode",
            "power": 0},
        "exp_prize": 50,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Dr. Mimi", 
        "hp": 70, 
        "base_atk": 10, 
        "gender": "clown doctor",
        "moves": {
            "name": "Clownin Around",
            "power": 15},
        "exp_prize": 50,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Hoarse E", 
        "hp": 20, 
        "base_atk": 5, 
        "gender": "weakling",
        "moves": {
            "name": "Spits",
            "power": 10},
        "exp_prize": 15,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Butter's Free", 
        "hp": 40, 
        "base_atk": 7, 
        "gender": "Free spirit",
        "moves": {
            "name": "fly hard",
            "power": 15},
        "exp_prize": 20,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Monkey", 
        "hp": 50, 
        "base_atk": 15, 
        "gender": "real life monkey",
        "moves": {
            "name": "Rips off arms",
            "power": 20},
        "exp_prize": 50,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Diddohnt", 
        "hp": 30, 
        "base_atk": 5, 
        "gender": "dirt lover",
        "moves": {
            "name": "Dirt mode",
            "power": 10},
        "exp_prize": 15,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Oh Mah Star", 
        "hp": 40, 
        "base_atk": 7, 
        "gender": "wide eye fossil",
        "moves": {
            "name": "Fossilize",
            "power": 10},
        "exp_prize": 25,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Poly Curl", 
        "hp": 40, 
        "base_atk": 7, 
        "gender": "round boi",
        "moves": {
            "name": "Spinning Belly",
            "power": 10},
        "exp_prize": 25,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Mar Veep", 
        "hp": 40, 
        "base_atk": 7, 
        "gender": "soft but tuff guy",
        "moves": {
            "name": "Wool Choke",
            "power": 10},
        "exp_prize": 25,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Vick Tary Bell", 
        "hp": 65, 
        "base_atk": 5, 
        "gender": "cup",
        "moves": {
            "name": "Leaf Slap",
            "power": 6},
        "exp_prize": 20,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Charlie", 
        "hp": 20, 
        "base_atk": 2, 
        "gender": "literal child",
        "moves": {
            "name": "Whine",
            "power": 5},
        "exp_prize": 10,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "WHOOP", 
        "hp": 50, 
        "base_atk": 10, 
        "gender": "mad-man",
        "moves": {
            "name": "Dunk",
            "power": 15},
        "exp_prize": 25,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Mudd Kiss", 
        "hp": 40, 
        "base_atk": 7, 
        "gender": "glompper",
        "moves": {
            "name": "Mud Kiss",
            "power": 10},
        "exp_prize": 17,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Banana", 
        "hp": 30, 
        "base_atk": 15, 
        "gender": "powerhouse",
        "moves": {
            "name": "Potassium",
            "power": 30},
        "exp_prize": 100,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Flair de Pon", 
        "hp": 45, 
        "base_atk": 10, 
        "gender": "fluff-o",
        "moves": {
            "name": "Cute attack",
            "power": 10},
        "exp_prize": 20,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Snake", 
        "hp": 35, 
        "base_atk": 7, 
        "gender": "piece of rope",
        "moves": {
            "name": "Big Bite",
            "power": 10},
        "exp_prize": 20,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Zappados", 
        "hp": 50, 
        "base_atk": 10, 
        "gender": "Sneaker Head",
        "moves": {
            "name": "Eletric Drip",
            "power": 10},
        "exp_prize": 30,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]},
    {
        "name": "Puggey Moto", 
        "hp": 30, 
        "base_atk": 7, 
        "gender": "suave bird",
        "moves": {
            "name": "Swoop",
            "power": 10},
        "exp_prize": 25,
        "art": [
            "         ▒▒▒▒▒▒▒▒ ",
            "       ▒▒▒▒▒▓▓▒▒▒▓",
            "  ▒▒▒  ▓▒▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒",
            " ▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒",
            "   ▒▒▒▓▒▒▒▒▒▒▓▓   ",
            "     ▒▒▒▒▒▒▒▓▒▒▒  ",
            "     ▒▒▒▒    ▒▒▒  "
        ]}
]
