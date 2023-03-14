from Player import Player
from Monster import Monster
from Save import Save
from mobGenerator import monsterPicker
from os import system as sys
from combat import combat



def main(playerCard:Player, monster:Monster):
    
    while True:
        playerCard, monster = Save(playerCard.name).load_state()
        sys('cls')
        if playerCard.status == "ready":
            print(playerCard)
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

        elif playerCard.status == "victory":
            print(playerCard)
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
                    playerCard, monster = Save(playerCard.name).load_state()
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
            

        elif playerCard.status == "defeat":
            print(playerCard)
            playGame = int(input(f"""Looks like {monster.name} whoooped your ass. What are you going to do about that?
                                                            
                                                            {playerCard.hp}/{playerCard.baseHP}
                                                            
                                                            1.Heal
                                                            2.Exit
                                                            
                                                        selection: """))
            try:
                if int(playGame) == 1:
                    sys('cle')
                    playerCard.heal_and_status()
                    continue
                elif int(playGame) == 2:
                    playerCard, monster = Save(playerCard.name).save_state(playerCard, monster)
                    playerCard.set_status('exit')
                    break
                exit()
            except ValueError:
                
                print("Invalid selection! Try again")
                continue
        
        elif playerCard.status == 'exit':
            exit()
            
