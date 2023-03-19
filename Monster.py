
class Monster():
    def __init__(self, name, lvl:int, hp:int, str:int, denf:int):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.str = str
        self.denf = denf
        self.atkPower = self.str + self.lvl * 2 
        self.blkPower = self.denf + self.denf * 2
        self.baseHP = self.hp
        
    # def monAttack(self, player:object, modifier:int=None):
    #     if modifier > 0:
    #         bonus = modifier
    #     else:
    #         pass
    #     dmg = self.atk + bonus - player.blkpwer
    #     player.hp -= dmg
    
    
    def healthUpdate(self, dmg:int=None):
        if dmg > 0:
            self.hp -= dmg
    
    def __str__(self):
        details = [self.name, self.lvl, self.hp, self.str, self.denf, self.atkPower, self.blkPower]
        
        test ="""
        Name    : {0}
        Level   : {1}
        HP      : {2}
        ATK     : {5}
        BLK     : {6}
        """.format(*details)
        
        return test
            