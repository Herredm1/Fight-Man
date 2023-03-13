import Player
import Monster
import shelve
import os

class Save():
    def __init__(self, fileName):
        self.fileName = fileName
        self.dir = f"./saves/{fileName}"
    
    def save_state(self,playerCard:Player, monster:Monster):
        with shelve.open(self.dir)as db:
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
                
                
                
                
                 
               
                
                
                
                