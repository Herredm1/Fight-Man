import Player
import Monster
import shelve
import os

class Save():
    def __init__(self, fileName):
        self.fileName = fileName
        self.dir = f"./saves/{fileName}"
    
    def set_option_monster(self, monster:Monster):
        with shelve.open(self.dir)as db:
            db['2'] = monster
        
    def set_option_player(self, playerCard:Player):
        with shelve.open(self.dir) as db:
            db['1'] = playerCard
          
            
    def get_option(self, playerCard:Player=object, monster:Monster=object):
        os.path.isfile(self.dir)
        print(self.dir)
        with shelve.open(self.dir) as db:
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
                
                
                
                
                 
               
                
                
                
                