from Monster import Monster
import os
from Save import Save

class Player():
    def __init__(self, name, lvl:int, str:int, denf:int, exp:int, status, baseXP:int=50):
        self.name = name
        self.lvl = lvl
        self.str = str 
        self.exp = exp
        self.denf = denf  
        self.baseEXP = baseXP
        self.baseHP = 50 + self.str + (self.denf * 2) + self.lvl
        self.atk = (self.str * 3 + self.lvl) 
        self.blkpwr = (self.denf * 3 + self.lvl)
        self.hp = self.baseHP
        self.status = status
        
    # Displays the characters Stats    
    def __str__(self):
        details = [self.name, self.lvl, self.hp, self.str, self.exp,self.denf, self.atk, self.blkpwr, self.baseHP, self.status, self.exp, self.baseEXP, self.lvl]
        
        test = """
        Name    : {0}
        STR     : {3}
        DEF     : {5}
        HP      : {2}/{8}
        EXP     : {10}/{11}  lVL:{12} 
        ATK     : {6}
        BLK     : {7}""".format(*details)
        
        return test
    def calculateBaseEXP(self):
        self.baseEXP = 50 * self.lvl
        

    # For future ATTRIBUTE Update
    def addSTR(self, num:int):
        self.str += num
    
    # For future ATTRIBUTE Update
    def addDFN(self, num:int):
        self.denf += num
    
    # For future LVL UP update    
    def addEXP(self, monster:Monster):
        self.calculateBaseEXP()
        results = self.lvl - monster.lvl
        xp_dict = {
            -1:5,
            0:10,
            1:15
        }
        xp = xp_dict[results]
        self.exp += xp
        if self.exp >= self.baseEXP:
            self.lvl += 1
            self.addSTR(1)
            self.addDFN(1)
            self.exp = 0
            self.calculateBaseEXP()
            
        else:
            pass
    
    # Might be what handles damage but unsure at this moment
    # def charAttack(self, monster:Monster, modifier:int=None):
    #     if modifier > 0:
    #         bonus = modifier
    #     else:
    #         pass
        
    #     dmg = self.atk + bonus - monster.blkpwr
    #     monster.hp -= dmg
            
    def set_status(self, status):
        self.status = status
        
    def heal_and_status(self):
        self.hp = self.baseHP
        if self.status =='defeat':
            self.status = 'ready'
        elif self.status == 'ready':
            pass
        else:
            self.status = 'victory'
    
    # How health is updated for combat and healing        
    def healthUpdate(self, dmg:int=0, heal:int=0):
        # try:
        if dmg > 0:
            self.hp -= dmg
            # For future death penalty
            # if self.hp <= 0:
            #     self.exp = 0
        else:
            pass
        
        # F0r future potion update
              
        if heal > 0:
            self.hp += heal
            if self.hp > self.baseHP:
                self.hp == self.baseHP

class CreateChacter():
    def __init__(self):
        pass
    
    def createChar(self, playerCard:Player, ):
        if os.path.exists('save.db.bak'):
            playerCard = Save('save.db').get_option(playerCard)
            return playerCard        
        else:
            print("No Save Detected. Moving to Character Creation.")
            playerCard = Player('temp',1,0,0,0,'new')
            
        points = 15
        while points > 0 and playerCard.status == 'new':
            playerName = input("What is your name Warrior: ")
            # try:
            might = int(input(f"""You have a total of {points}pts. How much Strength would you like? The remaing will be allocated to your DEF. """))
            if might > 14 or might == 0 or might == None:
                print("You've used too many points / Entered 0 / Entered nothing")
                continue
            elif might == 15:
                print("You must assign one point to Defense")
                continue
            elif might > 0:
                points -= might
                playerCard = Player(playerName, 1, might, points, 0, "ready")
                Save('save.db').set_option_player(playerCard)
                return playerCard
            # except:
            #     print("Invalid selection! Try again")
            #     continue