from Player import Player
from Save import Save
from mobGenerator import monsterPicker
from fight_statues import Status
from os import system as sys
from characterCreate import createChar


# playerCard Template
    
playerCard = Player("temp", 0, 0, 0, 0, "new")
createChar(playerCard)
playerCard = createChar(playerCard)

try:
    monster = ''
    monster = Save('save.db').get_option(monster=monster)
except:
    monster = monsterPicker(player=playerCard)
    Save('save.db').set_option_monster(monster=monster)


def main(playerCard:Player, monster):
    while playerCard.status in ['ready', 'victory', 'defeat','exit']:
        sys('cls')
        if playerCard.status == "ready":
            print(playerCard)
            Status().ready_status(playerCard, monster)
            

        elif playerCard.status == "victory":
            print(playerCard)
            Status().victory_status(playerCard, monster)
            

        elif playerCard.status == "defeat":
            print(playerCard)
            Status().defeat_status(playerCard, monster)
            
        elif playerCard.status == 'exit':
            exit()


main(playerCard,  monster)
