import shelve
import Player

class Save():
    def __init__(self, fileName):
        self.fileName = fileName
        
        
    def set_option(self, dict:dict):
        with shelve.open(self.fileName) as db:
            for k, v in dict.items():
                db.update({k:v})
            
    def get_option(self, player:object):
        with shelve.open(self.fileName) as db:
            print(db['name'])
            player.name = db['name']
            player.lvl = db['level']
            player.str = db['STR']
            player.denf = db['DEF']
            player.exp = db['EXP']
            player.status = db['status']
            
                
                
                
                
                 
               
                
                
                
                