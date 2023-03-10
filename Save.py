import shelve

class Save():
    def __init__(self, fileName):
        self.fileName = fileName
        
        
    def set_option(self, dict:dict):
        with shelve.open(self.fileName) as db:
            for k, v in dict.items():
                db.update({k:v})
            
    def get_option(self, dict:dict):
        with shelve.open(self.fileName) as db:
            dict.update(db)
            return dict