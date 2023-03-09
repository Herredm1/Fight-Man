class Player():
    def __init__(self, name, lvl:int, str:int, denf:int, exp:int, status, baseHP:int=None, hp:int=None,):
        self.name = name
        self.lvl = lvl
        self.str = str 
        self.exp = exp
        self.denf = denf  
        self.baseEXP = 50
        self.baseHP = 50 + self.str + self.denf * 2 + self.lvl
        self.atk = round((self.str + self.lvl) * 1.2)
        self.blkpwr = round((self.denf + self.lvl) * 1.2)
        self.hp = self.baseHP
        self.status = status

    # For future ATTRIBUTE Update
    def addSTR(self, num:int):
        self.str += num
    
    # For future ATTRIBUTE Update
    def addDFN(self, num:int):
        self.denf += num
    
    # For future LVL UP update    
    def addEXP(self, num:int):
        self.exp += num
        if self.exp >= self.baseEXP * (self.lvl * 2):
            self.lvl += 1
        else:
            pass
    
    # Might be what handles damage but unsure at this moment
    def charAttack(self, monster:object, modifier:int=None):
        if modifier > 0:
            bonus = modifier
        else:
            pass
        dmg = self.atk + bonus - monster.denf
        monster.hp -= dmg
    
    # Displays the characters Stats    
    def charDetail(self):
        details = [self.name, self.lvl, self.hp, self.str, self.exp,self.denf, self.atk, self.blkpwr]
        for detail in details:
            print(detail)
            
    def heal(self):
        if self.hp < self.baseHP:
            self.hp = self.baseHP
            # self.exp = self.baseEXP
    
    # How health is updated for combat and healing        
    def healthUpdate(self, dmg:int=0, heal:int=0):
        # try:
        if dmg > 0:
            self.hp -= dmg
        else:
            pass
        
        # F0r future potion update
              
        if heal > 0:
            self.hp += heal
            if self.hp > self.baseHP:
                self.hp == self.baseHP
