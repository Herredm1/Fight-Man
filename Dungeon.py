from Player import Player
from Monster import Monster
from globalFunctions import combat, monsterPicker
import random



class Dungeon:
    def __init__(self, dungeonName, dungeon_Area):
        self.dungeonName = dungeonName
        self.dungeon_Area = dungeon_Area
        
    
    def generateBattle(self, playerCard):
        
        dungeon_dict = {
            1: 'starter'
        }
        
        monsterLow_dict = {
            1: ['Rat', 'Slimes', 'Worm']
        }
        
        monsterMid_dict = {
            1:['SKeleton', 'Zombie','Ghost']
        }
        
        monsterHigh_dict = {
            1:['Spider', 'Goblin']
        }
        
        monsterBoss_Dict = {
            1:['Orc']
        }
        
        dungeon_Moster = random.choice()
        
        