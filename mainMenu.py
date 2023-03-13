from Player import Player
from Monster import Monster
from Save import Save
from characterCreate import createChar
import os
from main_game import main

directory = './saves/' 
extension = '.bak'  
              
files = [os.path.splitext(file)[0] for file in os.listdir(directory) if file.endswith(extension)]  

print(files)

while True:
    banner =''' █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████    ▄▄▄█████▓ ▒█████  
        ▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒
        ▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███      ▒ ▓██░ ▒░▒██░  ██▒
        ░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░
        ░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒     ▒██▒ ░ ░ ████▓▒░
        ░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░ 
        ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░       ░      ░ ▒ ▒░ 
        ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░        ░      ░ ░ ░ ▒  
            ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░                ░ ░  
                                ░                                                        
        █████▒██▓  ▄████  ██░ ██ ▄▄▄█████▓    ███▄ ▄███▓ ▄▄▄       ███▄    █           
        ▓██   ▒▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒   ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █           
        ▒████ ░▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░   ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒          
        ░▓█▒  ░░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░    ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒          
        ░▒█░   ░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░    ▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░          
        ▒ ░   ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░      ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒           
        ░      ▒ ░  ░   ░  ▒ ░▒░ ░    ░       ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░          
        ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░         ░      ░     ░   ▒      ░   ░ ░           
                ░        ░  ░  ░  ░                   ░         ░  ░         ░          
                
                
                                                                                            
                                                                                            '''
    
    print(banner)
                                                                                    

    options = ['New Game', 'Load Game', 'Exit']
    
    num = 1
    for option in options:
        print(f'{num}. {option}')
        num +=1 
    
    menu_selection = int(input('Option:'))
    
    if menu_selection == 1:
        createChar()
    if menu_selection == 2:
        select_dict = {}
        num =1
        for file in files:
            print(f'{num}. {file}')
            select_dict.update({num:file})
            num += 1
            
        load_option = int(input('Option:'))
            
        file = select_dict[load_option]    
        # Save(file).load_state()
        playerCard, monster = Save(file).load_state()
        
        main(playerCard, monster)
        