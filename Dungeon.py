from Player import Player
from Monster import Monster
from globalFunctions import combat, monsterPicker


class Dungeon:
    def __init__(self, dungeonName):
        self.dungeonName = dungeonName
        
    
    def generateBattle(self, playerCard):
        dungeon_dict = {
            1: 'starter'
        }