import Player
import Monster
import shelve
import sys

class Save():
    def __init__(self, fileName):
        self.fileName = fileName
        if sys.platform.startswith('win'):
            self.dir = f"./saves/{fileName}"
        else:
            self.dir = f"../saves/{fileName}"
    
    def save_state(self,playerCard:Player=None, monster:Monster=None):
        with shelve.open(self.dir)as db:
            if playerCard != None and monster == None:
                db['1'] = playerCard
                return playerCard
            elif playerCard == None and monster != None:
                db['2'] = monster
                return monster
            else:
                db['1'] = playerCard
                db['2'] = monster
                return playerCard, monster
                 
    def load_state(self):
        with shelve.open(self.dir) as db:
            playerCard = db['1']
            monster = db['2']
            return playerCard, monster
    
    def __str__(self):
        player = object()
        player = self.load_state()
        return str(player)
                
                
                
                
                 
               
                
                
                
                