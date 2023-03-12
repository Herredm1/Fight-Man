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
        while playerCard.status == 'ready':
            sys('cls')
            try:
                playGame = input(f"""                             What would you like to do
                                
                                        1. Fight
                                        2. Heal
                                        3. Exit & Save
                                        
                                        selection: """)
            
                if int(playGame) == 1:
                        monster = monsterPicker(player=playerCard)
                        combat(playerCard, monster)
                        break
                elif int(playGame) == 2:
                    playerCard.heal_and_status()
                    sys('cls')
                elif int(playGame) == 3:
                    Save('save.db').set_option_player(playerCard)
                    Save('save.db').set_option_monster(monster)
                    playerCard.set_status('exit')
                    return playerCard, monster
            except:
                print("Invalid selection. Please try again")
                
        
        
        
    def victory_status(self, playerCard:Player, monster:Monster):
        while playerCard.status == 'victory':
            try:
                playGame =input(
                        f"""
                                        That was amazaing! You defeated {monster.name}. What would you like to do
                                        
                                            {playerCard}
                                        
                                                    1. Fight
                                                    2. Heal
                                                    3. Exit 
                                                    
                                                selection: """
                    )
                if int(playGame) == 1:
                    picked_monster = monsterPicker(player=playerCard)
                    combat(playerCard, picked_monster)
                    break
                elif int(playGame) == 2:
                    playerCard.heal_and_status()
                    print(playerCard.hp)
                elif int(playGame) == 3:
                    Save('save.db').set_option_player(playerCard)
                    Save('save.db').set_option_monster(monster)
                    playerCard.set_status('exit')
            except:
                    print("Invalid selection. Please try again")
                    continue
                
    def defeat_status(self, playerCard:Player, monster:Monster):
        while playerCard.status == 'defeat':
                try:
                    playGame = input(f"""Looks like {monster.name} whoooped your ass. What are you going to do about that?
                                                        
                                                        {playerCard.hp}/{playerCard.baseHP}
                                                        
                                                        1.Heal
                                                        2.Exit
                                                        
                                                    selection: """
                        )
                    if int(playGame) == 1:
                        playerCard.heal_and_status()
                        break
                    elif int(playGame) == 2:
                        Save('save.db').set_option_player(playerCard)
                        Save('save.db').set_option_monster(monster)
                        playerCard.set_status('exit')
                        return playerCard, monster
                    exit()
                except:
                    print("Invalid selection! Try again")
    