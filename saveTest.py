from Player import Player
from Save import Save


def main():
    save = Save('save2.db')
    killo = Player('temp', 0 , 0, 0, 0, 'new')
    Killo_dict = {
        'name': killo.name,
        'level': killo.lvl,
        'STR': killo.str,
        'DEF': killo.denf,
        'EXP': killo.exp,
        'status': killo.status
            }
    q = int(input('1. Load  2. Save'))
    if q == 1:
        Killo_dict = {
            
                }   
        save.get_option(Killo_dict)
        print(Killo_dict)
        killo = Player(Killo_dict['name'], Killo_dict['level'] , Killo_dict['STR'], Killo_dict['DEF'], Killo_dict['EXP'], Killo_dict['status'])  
        print(killo)
        
    elif q == 2:
        
        save.set_option(Killo_dict)
        
main()

