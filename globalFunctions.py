from Monster import Monster
from Player import Player
from Save import Save
import random
import time
import os
import math
import sys
from glob import glob



def displayBanner():
    banner="""
 (  (             (                                     )          
 )\))(   '   (    )\                  )       (      ( /(          
((_)()\ )   ))\  ((_)   (     (      (       ))\     )\())   (     
_(())\_)() /((_)  _     )\    )\     )\  '  /((_)   (_))/    )\    
\ \((_)/ /(_))   | |   ((_)  ((_)  _((_))  (_))     | |_    ((_)   
 \ \/\/ / / -_)  | |  / _|  / _ \ | '  \() / -_)    |  _|  / _ \   
  \_/\_/  \___|  |_|  \__|  \___/ |_|_|_|  \___|     \__|  \___/   
                                                                   
 (                                     *                            
 )\ )                   )      )     (  `                           
(()/(   (    (  (    ( /(   ( /(     )\))(       )                  
 /(_))  )\   )\))(   )\())  )\())   ((_)()\   ( /(    (             
(_))_| ((_) ((_))\  ((_)\  (_))/    (_()((_)  )(_))   )\ )          
| |_    (_)  (()(_) | |(_) | |_     |  \/  | ((_)_   _(_/(          
| __|   | | / _` |  | ' \  |  _|    | |\/| | / _` | | ' \))         
|_|     |_| \__, |  |_||_|  \__|    |_|  |_| \__,_| |_||_| 

                                                                                        """
    return banner                        
                                                            
def roll_dice(): 
    die = random.randint(1,6)
    return die

def monsterPicker(player:Player):
    
    monsterNames = ["Kevin","Kelly","Mike","Daile","Marcile","Germain","Row","Gayla","Bobbe","Patrice","Lucia","Sorcha","Angela","Elvira","Sandie","Hedvige","Millie","Janina","Tasia","Daisi","Delia","Kessiah","Hyacinthia","Sybil","Zoe","Thia","Janaye","Dorothee","Trisha","Merilee","Zola","Anthe","Kellsie",]
    
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
                
                                                                                            
def combat(playerCard:Player, monster:Monster):
    clearScreen()
    print('')
    rowlength = len(f'#  Name: {playerCard.name:<20} Name: {monster.name}  #')
    width = len(monster.name) 
    if (rowlength % 2) == 1:
        print('# ' * math.ceil(rowlength / 2))
        print(f'#  Name: {playerCard.name:<20} Name: {monster.name}  #')
        print(f'#  LVL: {playerCard.lvl:<20}  LVL: {monster.lvl:<{width}}   #')
        print(f'#  HP: {playerCard.hp:<20}   HP: {monster.hp:<{width}}    #')
        print(f'#  ATK: {playerCard.atkPower:<20}  ATK: {monster.atkPower:<{width}}   #')
        print(f'#  BLK: {playerCard.blkPower:<20}  BLK: {monster.blkPower:<{width}}   #')
        print('# ' * math.ceil(rowlength / 2))
    else:
        print('# ' * math.ceil(rowlength / 2),'#', sep='')
        print(f'#  Name: {playerCard.name:<20}  Name: {monster.name}  #')
        print(f'#  LVL: {playerCard.lvl:<20}   LVL: {monster.lvl:<{width}}   #')
        print(f'#  HP: {playerCard.hp:<20}    HP: {monster.hp:<{width}}    #')
        print(f'#  ATK: {playerCard.atkPower:<20}   ATK: {monster.atkPower:<{width}}   #')
        print(f'#  BLK: {playerCard.blkPower:<20}   BLK: {monster.blkPower:<{width}}   #')
        print('# ' * math.ceil(rowlength / 2),'#', sep='')
    print('')
    while playerCard.hp > 0 or monster.hp > 0:
        die = roll_dice()
        time.sleep(1)
        dmg = playerCard.atkPower + die - monster.blkPower
        monster.healthUpdate(dmg=dmg)
        if dmg <= 0:
            print("You missed!")
        elif dmg > 0 and monster.hp > 0:
            print(f'Player Hit for: {dmg}. {monster.name} health at {monster.hp}')
        if monster.hp <= 0:
            monster.hp = 0
            print(f'Player Hit for: {dmg}. {monster.name} health at {monster.hp}')
            print(f'Congratulations! You have defeated {monster.name}')
            playerCard.set_status('victory')
            Save(playerCard.name).save_state(playerCard, monster)
            print('Heading back home')
            playerCard.addEXP(monster)
            time.sleep(3)
            return playerCard, monster
        time.sleep(1)
        die = roll_dice()
        time.sleep(1)
        dmg = monster.atkPower + die - playerCard.blkPower
        playerCard.healthUpdate(dmg=dmg, heal=0)
        if dmg <= 0:
            print(f"{monster.name} missed!")
        elif dmg > 0 and playerCard.hp > 0:
            print(f'{monster.name} Hit for: {dmg}. Player health at {playerCard.hp}')
        if playerCard.hp <= 0:
            playerCard.hp = 0
            print(f'{monster.name} Hit for: {dmg}. Player health at {playerCard.hp}')
            time.sleep(1)
            print(f'The mighty {playerCard.name} has been defeated by {monster.name}. Taking your character to the Hospital')
            playerCard.set_status('defeat')
            Save(playerCard.name).save_state(playerCard, monster)
            time.sleep(3)
            return playerCard, monster

def createChar():
    invalidChar = ['<', '>', ':','"', '/', '.','\\', '|', '?', '*',' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    clearScreen()
    points = 15
    while points > 0:
        try:
            playerName = input("What is your name Warrior: ")
            if not playerName:
                clearScreen()
                print('Your name cannot be empty Warrior')
                raise ValueError
            elif 10 < len(playerName):
                clearScreen()
                print('Your name has to be 10 characters or less')
                raise ValueError
            for x in playerName:
                if x in invalidChar:
                    clearScreen()
                    print('There is an invalid character in your name')
                    raise ValueError
                else:
                    continue
        except ValueError:
            input('Press Enter to try again...')
            clearScreen()
            continue
        try:
            might = int(input(f"""You have a total of {points}pts. How much Strength would you like? The remaing will be allocated to your DEF. """))
            if might > 14 or might == 0 or might == None:
                print("You've used too many points / Entered 0 / Entered nothing")
                continue
            elif might == 15:
                print("You must assign one point to Defense")
                continue
            elif might > 0:
                points -= might
                playerCard = Player(playerName, 1, might, points, 0, "ready")
                playerCard.calculateAtkDef()
                saveFile = playerCard.name
                monster = monsterPicker(player=playerCard)
                Save(saveFile).save_state(playerCard, monster)
                return playerCard, monster
        except ValueError:
            print("You've entered an Invalid character")
            time.sleep(2)
            clearScreen()
            continue
        
def refresh_load_files():
    if sys.platform.startswith('win'):
        directory = './saves/' 
        extension = '.bak'  
        files = [os.path.splitext(file)[0] for file in os.listdir(directory) if file.endswith(extension)]
        if os.path.exists(directory):
            pass
            return files
        else:
            os.mkdir(directory)
    else:
        directory = '/saves/'
        extension = '.db'
        if os.path.exists(directory):
            files = [os.path.splitext(file)[0] for file in os.listdir(directory) if file.endswith(extension)]
            return files
        else:
            os.mkdir(directory)
            

def clearScreen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
