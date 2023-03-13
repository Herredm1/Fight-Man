from Player import Player
from Save import Save
from main_game import main as playGame
from Monster import Monster
from mobGenerator import monsterPicker
from os import system as sys


def createChar():
    sys('cls')
    points = 15
    while points > 0:
        playerName = input("What is your name Warrior: ")
        # try:
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
            Save(saveFile).set_option_player(playerCard)
            monster = monsterPicker(player=playerCard)
            Save(saveFile).set_option_monster(monster=monster)
            playGame(playerCard=playerCard, monster=monster)
                