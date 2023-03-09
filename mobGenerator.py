import random
from Monster import Monster





def monsterPicker(monsterNames, levels, power, defense, player:object):

    Mlevel = random.choice(levels)
    if Mlevel == 0:
        Mlevel+=1
          
    health = random.randint(50, 100)
    block = random.choice(defense)
    damage = random.choice(power)
    name = random.choice(monsterNames)
    
    
    monster = Monster(name, Mlevel, health, damage, block)
    
    return monster    