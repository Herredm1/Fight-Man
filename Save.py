import Player
import Monster
import shelve

class Save():
    def __init__(self, fileName):
        self.fileName = fileName
        self.saveName = 'save.db'
    
    def set_option_monster(self, monster:Monster):
        with shelve.open(self.fileName)as db:
            db['2'] = monster
        
    def set_option_player(self, playerCard:Player):
        with shelve.open(self.fileName) as db:
            db['1'] = playerCard
          
            
    def get_option(self, playerCard:Player=None, monster:Monster=None):
        with shelve.open(self.fileName) as db:
            if playerCard != None:
                playerCard = db['1']
                item = playerCard
            elif monster != None:
                monster = db['2']
                item = monster
            return item
    
    def __str__(self):
        player = object()
        player = self.get_option(player)
        return str(player)
                
                
                
                
                 
               
                
                
                
                