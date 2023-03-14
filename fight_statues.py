from Player import Player
from Monster import Monster
from mobGenerator import monsterPicker
from combat import combat
from Save import Save
from os import system as sys



class Status:
    def __init__(self):
        pass
        
    
    def ready_status(self, playerCard:Player, monster:Monster):
        sys('cls')
        while playerCard.status == 'ready':
            playGame = input(f"""                             What would you like to do
                                
                                        1. Fight
                                        2. Heal
                                        3. Exit & Save
                                        
                                        selection: """)
            
            try:
                if int(playGame) == 1:
                    monster = monsterPicker(player=playerCard)
                    combat(playerCard, monster)
                elif int(playGame) == 2:
                    playerCard.heal_and_status()
                    sys('cls')
                elif int(playGame) == 3:
                    Save(playerCard.name).save_state(playerCard, monster)
                    playerCard.set_status('exit')
            except ValueError:
                print("Invalid selection. Please try again")
                
        
        
        
    def victory_status(self, playerCard:Player, monster:Monster):
        sys('cls')
        while playerCard.status == 'victory':
            playGame =input(
                        f"""
                                        That was amazaing! You defeated {monster.name}. What would you like to do
                                        
                                            {playerCard}
                                        
                                                    1. Fight
                                                    2. Heal
                                                    3. Exit 
                                                    
                                                selection: """
                    )
            try:
                if int(playGame) == 1:
                    picked_monster = monsterPicker(player=playerCard)
                    combat(playerCard, picked_monster)
                elif int(playGame) == 2:
                    playerCard.heal_and_status()
                    print(playerCard.hp)
                elif int(playGame) == 3:
                    Save(playerCard.name).save_state(playerCard, monster)
                    playerCard.set_status('exit')
                    return playerCard, monster
            except ValueError:
                    print("Invalid selection. Please try again")
                    continue
                
    def defeat_status(self, playerCard:Player, monster:Monster):
        while playerCard.status == 'defeat':
                playGame = input(f"""Looks like {monster.name} whoooped your ass. What are you going to do about that?
                                                        
                                                        {playerCard.hp}/{playerCard.baseHP}
                                                        
                                                        1.Heal
                                                        2.Exit
                                                        
                                                    selection: """
                        )
                try:
                    if int(playGame) == 1:
                        sys('cle')
                        playerCard.heal_and_status()
                        break
                    elif int(playGame) == 2:
                        playerCard, monster = Save(playerCard.name).save_state(playerCard, monster)
                        playerCard.set_status('exit')
                        break
                    exit()
                except ValueError:
                    print("Invalid selection! Try again")
    