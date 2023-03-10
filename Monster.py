
class Monster():
    def __init__(self, name, lvl:int, hp:int, str:int, denf:int):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.str = str
        self.denf = denf
        self.atk = round((self.str + self.lvl )* 1.2 )
        self.blkpwr = round((self.denf + self.denf) * 1.2)
        
    def monAttack(self, player:object, modifier:int=None):
        if modifier > 0:
            bonus = modifier
        else:
            pass
        dmg = self.atk + bonus - player.blkpwer
        player.hp -= dmg
    
    def healthUpdate(self, dmg:int=None):
        if dmg > 0:
            self.hp -= dmg
    
    def charDetail(self):
        details = [self.name, self.lvl, self.hp, self.str, self.denf, self.atk, self.blkpwr]
        for detail in details:
            print(detail)