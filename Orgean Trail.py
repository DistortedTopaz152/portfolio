#Dyson Smith & Daniel Lehman
#Nov. 5 2020
#Orgean Trail

def credits_logo():
    TITLE = '''╔════╗╔╗ ╔╗╔═══╗    ╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═╗ ╔╗    ╔════╗╔═══╗╔═══╗╔══╗╔╗   
║╔╗╔╗║║║ ║║║╔══╝    ║╔═╗║║╔═╗║║╔══╝║╔═╗║║╔═╗║║║╚╗║║    ║╔╗╔╗║║╔═╗║║╔═╗║╚╣╠╝║║   
╚╝║║╚╝║╚═╝║║╚══╗    ║║ ║║║╚═╝║║╚══╗║║ ╚╝║║ ║║║╔╗╚╝║    ╚╝║║╚╝║╚═╝║║║ ║║ ║║ ║║   
  ║║  ║╔═╗║║╔══╝    ║║ ║║║╔╗╔╝║╔══╝║║╔═╗║║ ║║║║╚╗║║      ║║  ║╔╗╔╝║╚═╝║ ║║ ║║ ╔╗
 ╔╝╚╗ ║║ ║║║╚══╗    ║╚═╝║║║║╚╗║╚══╗║╚╩═║║╚═╝║║║ ║║║     ╔╝╚╗ ║║║╚╗║╔═╗║╔╣╠╗║╚═╝║
 ╚══╝ ╚╝ ╚╝╚═══╝    ╚═══╝╚╝╚═╝╚═══╝╚═══╝╚═══╝╚╝ ╚═╝     ╚══╝ ╚╝╚═╝╚╝ ╚╝╚══╝╚═══╝                                                                          
 '''
    LOGO = '''                                       ,,.                                      
                                    ...,,....                                   
                                 ......,,......                                 
                              .@@@@@@@@@@@@@@@@...                              
                      @@@@@@@.....@@@@@@@@@@@@...@@@@@@@*                       
                %@@@@    ,.......@@@@@@@@@@@@@@.......,. &@@@@                  
             @@@         ..,,..@@@@@@@@@@@@@@@@@%..,,..       @@@&              
          %@@            .....,@@@@@@@@@@@@@@@@@@,.....          @@@            
        *@@.             .....@@@@@@@@@@@@@@@@@@@#.....           *@@@          
       ,@@               .....@@@@@@@@@@@@@@@@@@@@.....            (@@@         
       @@/               .....@@@@@@@@@@@@@@@@@@@@.....             @@@         
       @@/               .....@@@@@@@@@@@@@@@@@@@@.....             @@@         
        @@,              .....@@@@@@@@@@@@@@@@@@@#.....            (@@          
          @@             .....*@@@@@@@@@@@@@@@@@@,.....           @@*           
            @@@          ....,,@@@@@@@@@@@@@@@@@&,,....        &@@@             
              /@@@@      ..,,...@@@@@@@@@@@@@@@@...,,,.    @@@@@                
                   ,@@@@@@,.......@@@@@@@@@@@@,.....@@@@@@@&                    
                             @@@@@@@@@@@@@@@@@@@@@@@@                           
                               .........,........                               
                                  ......,.....                                  
                                     ...,...                                    
                                       .,                                       '''
    CREDITS = 'Daniel Lehman & Dyson Smith created this vertion of "The Oregon Trail"'
    print(TITLE)
    print(LOGO)
    print(CREDITS)

def main_menu():
  option1 = 'Travle the trail'
  option2 ='Learn about the trail'
  option3 = 'Quit out'
  options = [option1,option2,option3]
  
  while True:
    choice = display_options(options)
    if choice == 1:
      break
    elif choice == 2:
      learn()
    elif choice ==3:
      quit_out()
  play_game()

def display_options(options):
  index = 1
  for option in options:
    print(str.format('{}......{}',index,option))
    index+=1
  while True:
    choice = input('pick an number between 1 and'+str(len(options))+":")
    if choice.isnumeric():
      choice = int(choice)
      if choice >= 1 and choice <= len(options):
        return choice
      else:
        print('Not an option')
    else:
        print('Not an option')
    
def learn():
    print("""\nTry taking a journey by covered wagon across 2000 miles of plains, rivers, and mountains. Try!
    on the plains, will you slosh your oxen through muck and water-filled ruts or will you plod through dust
    six inches deep?""")
    input("Press enter to continue")
    print(""""\nHow will you cross the rivers? If you have money, you might take a ferry (if there is a ferry).
    Or you can ford the river and hope you and your wagon arn't swallowed alive.""")
    input("Press enter to continue")
    print("""\nWhat about supplies? Well if your low on food you can hunt. You might buffalo or a bear in the mountains.
    At the Dalles, better take the Barlow Road. If you die, don't give up.""")
    input('\nif you want to quit the game press Q')

def quit_out():
    choice = input('\nPress Q to escape program')
    if choice == 'q': 
        exit()

def play_game():
    pass


#main game
credits_logo()
main_menu()
input()
