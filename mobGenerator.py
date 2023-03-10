import random
from Monster import Monster
from Player import Player

def monsterPicker(player:Player):
    
    monsterNames = [
    "Kevin",
    "Kelly",
    "Mike",
    "Daile",
    "Marcile",
    "Germain",
    "Row",
    "Gayla",
    "Bobbe",
    "Patrice",
    "Lucia",
    "Sorcha",
    "Angela",
    "Elvira",
    "Sandie",
    "Hedvige",
    "Millie",
    "Janina",
    "Tasia",
    "Daisi",
    "Delia",
    "Kessiah",
    "Hyacinthia",
    "Sybil",
    "Zoe",
    "Thia",
    "Janaye",
    "Dorothee",
    "Trisha",
    "Merilee",
    "Zola",
    "Anthe",
    "Kellsie",
]
    
    playerCard = player
    
    levels = [playerCard.lvl - 1, playerCard.lvl, playerCard.lvl + 1]
    power = [playerCard.str - 1, playerCard.str, playerCard.str + 1]
    defense = [playerCard.denf - 1, playerCard.denf, playerCard.denf + 1]

    Mlevel = random.choice(levels)
    if Mlevel == 0:
        Mlevel+=1
          
    health = random.randint(50, 100)
    block = random.choice(defense)
    damage = random.choice(power)
    name = random.choice(monsterNames)
    
    
    monster = Monster(name, Mlevel, health, damage, block)
    
    return monster    