from roll import roll_dice
import time
from Player import Player
from Monster import Monster
 

def combat(player:Player, monster:Monster):
    while player.hp > 0 and monster.hp > 0:
        die = roll_dice()
        # print(f'Die Value: {die}')
        time.sleep(1)
        dmg = player.atk + die - monster.blkpwr
        monster.healthUpdate(dmg=dmg)
        if dmg <= 0:
            print("You missed!")
        elif dmg > 0 and monster.hp > 0:
            print(f'Player Hit for: {dmg}. {monster.name} health at {monster.hp}')
        if monster.hp <= 0:
            monster.hp = 0
            print(f'Player Hit for: {dmg}. {monster.name} health at {monster.hp}')
            print(f'Congratulations! You have defeated {monster.name}')
            print('Heading back home')
            player.set_status('victory')
            input("Press enter to continue....")
            break
        time.sleep(1)
        die = roll_dice()
        # print(f'Die Value: {die}')
        time.sleep(1)
        dmg = round((monster.atk + die) * 1.5 - player.blkpwr)
        player.healthUpdate(dmg=dmg, heal=0)
        if dmg <= 0:
            print(f"{monster.name} missed!")
        elif dmg > 0 and player.hp > 0:
            print(f'{monster.name} Hit for: {dmg}. Player health at {player.hp}')
        if player.hp <= 0:
            player.hp = 0
            print(f'{monster.name} Hit for: {dmg}. Player health at {player.hp}')
            time.sleep(1)
            player.set_status('defeat')
            print(f'The mighty {player.name} has been defeated by {monster.name}. Taking your character to the Hospital')
            input('Press enter to continue....')
            break
        