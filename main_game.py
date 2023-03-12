from Player import Player, CreateChacter
from Save import Save
from mobGenerator import monsterPicker
from fight_statues import Status
from os import system as sys


# playerCard Template
playerCard = Player("temp", 0, 0, 0, 0, "new")
CreateChacter().createChar(playerCard)
playerCard = CreateChacter().createChar(playerCard)

try:
    monster = ''
    monster = Save('save.db').get_option(monster=monster)
except:
    monster = monsterPicker(player=playerCard)
    Save('Save.db').set_option_monster(monster=monster)
    
print(playerCard)


def main(playerCard:Player, monster):
    while playerCard.status in ['ready', 'victory', 'defeat','exit']:
        sys('cls')
        if playerCard.status == "ready":
            Status().ready_status(playerCard, monster)
            

        elif playerCard.status == "victory":
            sys('cls')
            Status().victory_status(playerCard, monster)
            

        elif playerCard.status == "defeat":
            sys('cls')
            # monster = Save('save.db').get_option(monster=monster)
            Status().defeat_status(playerCard, monster)
            
        elif playerCard.status == 'exit':
            exit()


main(playerCard,  monster)
