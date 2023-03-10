from Player import Player
from mobGenerator import monsterPicker
from combat import combat
from os import system as sys
from Save import Save


# playerCard Template
playerCard = Player("temp", 0, 0, 0, 0, "new")
try:
    Save('save.db').get_option(playerCard)
    playerCard = Save('save.db').get_option(playerCard)
except:
    pass

# Temporary Main function
def main(playerCard:Player):
    points = 15
    while points > 0 and playerCard.status == 'new':
        if playerCard.status == "new":
            playerName = input("What is your name Warrior: ")
            while points > 0:
                try:
                    might = int(input("How much Strength would you like: "))
                    points -= might
                    if might > 14 or might == 0 or might == None:
                        print("You've used too many points / Entered 0 / Entered nothing")
                        points= 15
                        continue
                    elif might == 15:
                        print("You must assign one point to Defense")
                        continue
                    elif might > 0:
                        print(f"You have {points} points to spend")
                        playerCard.addSTR(might)
                except:
                    print("Invalid selection! Try again")
                    continue      
                try:  
                    protect = int(input("How much Defense would you like: "))
                    points -= protect
                    if protect + might > 15 or protect == 0 or protect == None:
                        print("You've used too many points / Entered 0 / Entered nothing")
                    elif points == 0:
                        playerCard.addDFN(protect)
                        playerCard = Player(playerName, 1, might, protect, 0, 'ready')
                        Save('save.db').set_option(playerCard)
                        print(playerCard.status)
                        break
                    elif points > 0 or points == 0:
                        points -= protect
                        playerCard.addDFN(protect)
                        continue
                except:
                    print("Invalid selection! Try again")
                    continue
                
    while playerCard.status in ['ready', 'victory', 'defeat']:
        sys('cls')
        if playerCard.status == "ready":
            playGame = input(f"""                             What would you like to do
                             {playerCard}
                                    1. Fight
                                    2. Heal
                                    3. Exit & Save
                                    
                                    selection: """)
        
            if int(playGame) == 1:
                picked_monster = monsterPicker(player=playerCard)
                combat(playerCard, picked_monster)
            elif int(playGame) == 2:
                playerCard.heal_and_status()
                playerCard.status = "ready"
                sys('cls')
            elif int(playGame) == 3:
                Save('save.db').set_option(playerCard)

        elif playerCard.status == "victory":
            sys("cls")
            try:
                playGame =input(
                        f"""
                                        That was amazaing! You defeated {picked_monster.name}. What would you like to do
                                        
                                            {playerCard}
                                        
                                                    1. Fight
                                                    2. Heal
                                                    3. Exit 
                                                    
                                                selection: """
                    )
                if int(playGame) == 1:
                    picked_monster = monsterPicker(playerCard=playerCard)
                    combat(playerCard, picked_monster)
                elif int(playGame) == 2:
                    playerCard.heal_and_status()
                    print(playerCard.hp)
                elif int(playGame) == 3:
                    Save('save.db').set_option(playerCard)
                    break
            except:
                playGame =input(
                        f"""
                                        Welcome back! Are you ready to fight again?. What would you like to do
                                        
                                            {playerCard}
                                        
                                                    1. Fight
                                                    2. Heal
                                                    3. Exit 
                                                    
                                                selection: """
                    )
                if int(playGame) == 1:
                    picked_monster = monsterPicker(playerCard=playerCard)
                    combat(playerCard, picked_monster)
                elif int(playGame) == 2:
                    playerCard.heal_and_status()
                    print(playerCard.hp)
                    playerCard.status = "ready"
                elif int(playGame) == 3:
                    Save('save.db').set_option(playerCard)
                    break
            if playerCard.hp <= 0:
                playerCard.status = "defeat"
                pass

        elif playerCard.status == "defeat":
            sys("cls")
            try:
                playGame = input(
                        f"""Looks like {picked_monster.name} whoooped your ass. What are you going to do about that?
                                                    
                                                    {playerCard.hp}/{playerCard.baseHP}
                                                    
                                                    1.Heal
                                                    2.Exit
                                                    
                                                selection: """
                    )
                if int(playGame) == 1:
                    playerCard.heal_and_status()
                    playerCard.status = "ready"
                    sys('cls')
                elif int(playGame) == 2:
                    Save('save.db').set_option(playerCard)
                    break
                print("Invalid selection! Try again")
                continue
            except:
                playGame =input(
                        f"""Welcome back, you're currently in the hospital. What would you like to do??
                                                    
                                                    1.Heal
                                                    2.Exit
                                                    
                                                selection: """
                    )
                if int(playGame) == 1:
                    playerCard.heal_and_status()
                    playerCard.status = "ready"
                    sys('cls')
                elif int(playGame) == 2:
                    Save('save.db').set_option(playerCard)
                    break
                print("Invalid selection! Try again")
                continue
    exit()


main(playerCard)
