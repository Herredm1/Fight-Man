from Player import Player
from mobGenerator import monsterPicker
from combat import combat
from os import system as sys


# Player Template       
player = Player('temp', 1 , 0, 0, 0, 'new')

# For future Inventory update
inventory = []

# List of monster names that random pulls from. Will add this to the monsterPicker function later
monsterNames = ['Kevin','Kelly','Mike','Daile', 'Marcile', 'Germain', 'Row', 'Gayla', 'Bobbe', 'Patrice', 'Lucia', 'Sorcha', 'Angela', 'Elvira', 'Sandie', 'Hedvige', 'Millie', 'Janina', 'Tasia', 'Daisi', 'Delia', 'Kessiah', 'Hyacinthia', 'Sybil', 'Zoe', 'Thia', 'Janaye', 'Dorothee', 'Trisha', 'Merilee', 'Zola', 'Anthe', 'Kellsie']

# Monster vairables. Will move to the monsterPicker function later.
levels =  [player.lvl - 1 , player.lvl, player.lvl + 1]
power = [player.str - 1 , player.str, player.str + 1]
defense = [player.denf - 1 , player.denf, player.denf + 1]

# Temporary Main function
def main(player:object):

    while True:
        points = 15
        if player.status == 'new':
            playerName = input("What is your name Warrior: ")
            while points > 0:
                print(f"You have {points} points to spend")
                try:
                    might = int(input("How much Strength would you like: "))
                    points -= might
                    if might >= 15 or might == 0 or might == None:
                        points = 15
                        print("At least 1 point needs to be spent on Defense")
                        continue
                    elif points <= 0:
                        break
                    print(f"{points} remaining")
                    protect = int(input('How much Defense would you like: '))
                    points -= protect
                    if protect == 15:
                        print("At least one point must be spent on Attack")
                        points = 15
                    elif points < 0:
                        print("You used too many points. Restarting skills selection.")
                        might = 0
                        protect = 0
                        points= 15
                        continue
                    elif points == 0:
                        break
                except:
                    print("Invalid selection! Try again")
                    continue
            status = 'ready'
            player = Player(playerName, 1, might, protect, 0, status)
        elif player.status == 'ready':
            sys('cls')
            while player.status == 'ready':
                try:    
                    playGame = int(input(f"""
                                    What would you like to do
                                         
                                    {player}
                                    
                                            1. Fight
                                            2. Save
                                            3. Exit
                                            
                                        selection: """))
                    if playGame == 1:
                        picked_monster = monsterPicker(monsterNames, levels, power, defense, player)
                        combat(player, picked_monster)
                    elif playGame == 2:
                        sys.exit()
                    
                except:
                    print("Invalid selection! Try again")
                    continue
                if player.hp <= 0:
                    player.status = 'defeat'
                else:
                    player.status = 'victory'                
        elif player.status == 'victory':
                sys('cls')
                try:
                    playGame = int(input(f"""
                                         That was amazaing! You defeated {picked_monster.name}. What would you like to do
                                        
                                            {player}
                                        
                                                    1. Fight
                                                    2. Heal
                                                    3. Exit 
                                                    
                                                selection: """))
                    if playGame == 1:
                        picked_monster = monsterPicker(monsterNames, levels, power, defense, player)
                        combat(player, picked_monster)
                    if playGame == 2:
                        player.heal()
                        print(player.hp)
                        player.status = 'ready'
                except:
                    print("Invalid selection! Try again")
                    continue
                
                if player.hp <= 0:
                    player.status = 'defeat'
                
        elif player.status == 'defeat':
            sys('cls')
            try:
                playGame = int(input(f'''Looks like {picked_monster.name} whoooped your ass. What are you going to do about that?
                                                    
                                                    1.Heal
                                                    2.Exit
                                                    
                                                selection: '''))
                if playGame == 1:
                    player.heal()
                    player.status = 'ready'
                elif playGame == 2:
                    sys.exit()
            except:
                print("Invalid selection! Try again")
                continue
main(player)