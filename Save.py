import shelve
import Player
import os

class Save():
    def __init__(self, fileName):
        self.fileName = fileName
        self.saveName = 'save.db.bak'
        
    def set_option(self, player:object):
        if os.path.exists(self.saveName):
            with shelve.open(self.fileName) as db:
                db['1'] = player   
        else:
            print("No Save Detected. Moving to Character Creation.")
            
    def get_option(self, player:object):
        with shelve.open(self.fileName) as db:
            player = db['1']
            return player
    
    def __str__(self):
        player = object()
        player = self.get_option(player)
        return str(player)
                
                
                
                
                 
               
                
                
                
                