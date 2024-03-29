import Save
import time
import globalFunctions
import main_game

def menu():
    while True:
        save_files = globalFunctions.refresh_load_files()
        globalFunctions.clearScreen()
        try:
            banner = globalFunctions.displayBanner()
            print(banner)
            
            options = ['New Game', 'Load Game', 'Exit']
            
            num = 1
            for option in options:
                print(f'                               {num}. {option}')
                num +=1 
            
            menu_selection = int(input('''                                        
                                Option:'''))
            
            # Pressing 1 will bring you to the Character Creation.
            if menu_selection == 1:
                playerCard, monster = globalFunctions.createChar()
                main_game.main(playerCard, monster)
                
            # Pressing 2 will bring you into the load game selection.
            elif menu_selection == 2:
                while menu_selection == 2:
                    save_files = globalFunctions.refresh_load_files()
                    globalFunctions.clearScreen()
                    print(banner)
                    if len(save_files) == 0:
                        print("There are no Saves")
                        time.sleep(2)
                        break
                    try:
                        select_dict = {}
                        num =1
                        for file in save_files:
                            print(f'{num}. {file}')
                            select_dict.update({num:file})
                            num += 1
                        print(f'''{num}. Exit''')  
                        load_option = int(input('Option:'))
                        if load_option is num:
                            break
                        elif load_option in select_dict:
                            file = select_dict[load_option]
                        else:
                            raise KeyError    
                        playerCard, monster = Save.Save(file).load_state()
                        main_game.main(playerCard, monster)
                        break
                    except KeyError:
                        print("Invalid selection! Try again")
                        time.sleep(2)
                        continue
                                  
            # exit the program if the user selects option 3            
            elif menu_selection == 3: 
                exit()
        except ValueError:
            print("Invalid selection! Try again")
            time.sleep(2)
            continue
menu()       