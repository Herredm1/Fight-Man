from Player import Player
from Save import Save
import os

def createChar(playerCard:Player):
        if os.path.exists('save.db.bak'):
            playerCard = Save('save.db').get_option(playerCard)
            return playerCard        
        else:
            print("No Save Detected. Moving to Character Creation.")
            playerCard = Player('temp',1,0,0,0,'new')
            
        points = 15
        while points > 0 and playerCard.status == 'new':
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
                Save('save.db').set_option_player(playerCard)
                playerCard.calculateAtkDef()
                return playerCard