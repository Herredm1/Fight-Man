import Save
import time
import globalFunctions
import os
import main_game



def menu():
    directory = './saves/' 
    extension = '.bak'  
    if os.path.exists(directory):
        pass
    else:
        os.mkdir(directory)
                
    files = [os.path.splitext(file)[0] for file in os.listdir(directory) if file.endswith(extension)]  
    
    while True:
        os.system('cls')
        try:
            banner = globalFunctions.displayBanner()
            print(banner)
                                                                                            
    
            options = ['New Game', 'Load Game', 'Exit']
            
            num = 1
            for option in options:
                print('                         ',f'{num}. {option}')
                num +=1 
            
            menu_selection = int(input('Option:'))
            
            if menu_selection == 1:
                playerCard, monster = globalFunctions.createChar()
                main_game.main(playerCard, monster)
            elif menu_selection == 2:
                while menu_selection == 2:
                    os.system('cls')
                    print(banner)
                    if len(files) == 0:
                        print("There are no Saves")
                        time.sleep(2)
                        break
                    try:
                        select_dict = {}
                        num =1
                        for file in files:
                            print(f'{num}. {file}')
                            select_dict.update({num:file})
                            num += 1  
                        load_option = int(input('Option:'))
                        file = select_dict[load_option]    
                        playerCard, monster = Save.Save(file).load_state()
                        main_game.main(playerCard, monster)
                        break
                    except:
                        print("Invalid selection! Try again")
                        time.sleep(2)
                        continue
            elif menu_selection == 3:
                exit()
        except ValueError:
            print("Invalid selection! Try again")
            time.sleep(2)
            continue
menu()       