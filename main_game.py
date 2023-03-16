from Player import Player
from Monster import Monster
from Save import Save
from os import system as sys
from globalFunctions import monsterPicker, combat
import time


def main(playerCard:Player, monster:Monster):
    while True:
        pINFO = [playerCard.name, playerCard.lvl, playerCard.hp,playerCard.baseHP, playerCard.atkPower, playerCard.blkPower, playerCard.str, playerCard.denf,'Fight', 'Heal', 'Exit to Main Menu', monster.name, playerCard.exp, playerCard.baseEXP]
        sys('cls')
        if playerCard.status == "ready":
            banner = '''                                     What would you like to do?
            {0}
            LVL : {1}
            HP  : {2}/{3}                                1.{8}
            ATK : {4}                                   2. {10}
            BLK : {5}                                   
            STR : {6}
            DFN : {7}
            XP  : {12}/{13}
                                                                                    '''.format(*pINFO)
            print(banner)
            playGame = input('Selection: ')
            
            try:
                if int(playGame) == 1:
                    monster = monsterPicker(player=playerCard)
                    playerCard, monster = combat(playerCard, monster)
                elif int(playGame) == 2:
                    Save(playerCard.name).save_state(playerCard, monster)
                    return playerCard, monster
            except ValueError:
                print("Invalid selection. Please try again")

        elif playerCard.status == "victory":
            sys('cls')
            banner = '''        That was an Epic fight! {11} didn't even stand a chance. What would you like to do?
        
        
        {0}
        LVL : {1}                                    1. {8}
        HP  : {2}/{3}                                2. {9}
        ATK : {4}                                   3. {10}
        BLK : {5}                                    
        STR : {6}
        DFN : {7}
        XP  : {12}/{13}
            
                                                                                        '''.format(*pINFO)
            print(banner)
            playGame= input('Selection: ')
            try:
                if int(playGame) == 1:
                    monster = monsterPicker(player=playerCard)
                    playerCard, monster = combat(playerCard, monster)
                    continue
                elif int(playGame) == 2:
                    playerCard.heal_and_status()
                    continue
                elif int(playGame) == 3:
                    Save(playerCard.name).save_state(playerCard, monster)
                    return playerCard, monster
            except ValueError:
                    print("Invalid selection. Please try again")
                    continue
            

        elif playerCard.status == "defeat":
            sys('cls')
            print(playerCard)
            banner = '''You're now in the Hospital. You were defeated by {11}. What would you like to do?
        
        
        LVL : {1}
        HP  : {2}/{3}                           
        ATK : {4}                               1. {9}
        BLK : {5}                               2. {10}
        STR : {6}
        DFN : {7}
        XP  : {12}/{13}
                                                                                        '''.format(*pINFO)
            print(banner)
            playGame= input('Selection: ')
            try:
                if int(playGame) == 1:
                    sys('cle')
                    playerCard.heal_and_status()
                    continue
                elif int(playGame) == 2:
                    playerCard, monster = Save(playerCard.name).save_state(playerCard, monster)
                    return
            except ValueError:
                print("Invalid selection! Try again")
                time.sleep(2)
                continue
