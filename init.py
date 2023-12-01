import os
from os import system, name 
import sys 
import argparse

import backend as backend 
from backend.scenario import Scenario 

""" TC API Logo. """
logo = (r''' 
  _____________________________  
 |                             | 
 |                             | 
 |___________       ___________| 
            |       |       ___________________
            |       |      |                   |
            |       |      |     ___________   |
            |       |      |     |         |___|
            |       |      |     |
            |       |      |     |          ___
            |       |      |     |_________|   |
            |       |      |                   |
            |_______|      |___________________|

 -----------------------------------------------------
|    Laboratory Application Programming Interface     |
 -----------------------------------------------------
''')

""" Shows the logo. 

@return null
"""
def showLogo(): 
    print(logo)

""" Clears the screen. 

@return null
"""
def clearScreen():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

""" Resets the screen.

@return null
"""
def resetScreen(): 
    clearScreen()
    showLogo()

""" Displays information on stoping the server. 

@return null
"""
def stoping_server_info(): 
    print()

""" Displays information on clearing server databases.

@return null
"""
def clear_data_info(): 
    print()

""" Displays information on updating the server. 

@return null
"""
def update_server_info(): 
    
    resetScreen()
    
    print()
    print(

        "\n   This API will be stored publicly on GitHub. Updating the\n"
        "server relies on the existence of an update as well as a secure\n" 
        "internet connectivity. "

    )

""" Displays information on starting the server. 

@return null
"""
def start_server_info(): 
    resetScreen()

    print() 
    print(

        " To start the TC Laboratory Application Programming \n"
        "Interface (LAPI), execute this program again, but instead\n"
        "of the help flag, specify the virtual flag. This will\n"
        "create the virtual structure necessary to correctly\n"
        "run LAPI by downloading all required packages. Once the\n"
        "virtual environment is activated with clear, you can\n"
        "now run LAPI on port 5000."
        
    )

""" Displays user information. 

@return null
"""
def user_info():
    resetScreen()

    print() 
    print(

        "   User credentials should be stored in the admin.csv \n"
        "file. TC Engineers have provided a static file location\n"
        "for this.\n\n"
        
        "Please do NOT move it."

    )

""" Shows available commands and troubleshot routes. 

@return null
"""
def help():

    running = True
    while running: 

        resetScreen()
        background()

        print("\nFor more information choose one of the following.")


        print("1) Starting the server ")
        print("2) Updating the server ")
        print("3) Stoping the server ")
        print("4) Clearing the database ")
        print("5) Users. ")
        print("6) Quit") 

        choice = input("\nChoose: ")

        """Condition dependent on choice. """
        if choice == '6':
            running = False
        elif choice == '5': 
            user_info()
            input()
        elif choice == '4': 
            clear_data_info()
            input()
        elif choice == '3': 
            stoping_server_info()
            input()
        elif choice == '2': 
            update_server_info()
            input()
        elif choice == '1': 
            start_server_info()
            input() 

""" Gives some background on the application. 

@return null
"""
def background():
    clearScreen()
    showLogo()

    print(

        "   The TC Lab API is an application programming interface\n"
        "utilizing the Flask framework. This open source technology\n"
        "allowed TC technology to react to various activities\n"
        "occuring on other nodes on the network. The reason for\n"
        "implementing this as a development server is because of\n"
        "is range of application. Flask APIs are rather readable, \n"
        "dependable, extendable, and handy teaching tools. Many\n"
        "instruments and devices on the TC network will communicate\n"
        "through this API using common HTTP methods. "
    )

""" Describes available utilities and scenarios. 

@return null
"""
def utilities(): 

    resetScreen() 

    print()
    print(

        "The following utilities will be facilitated through  \n"
        "this API. Client applications will be provided seperately.\n\n"
        "1) Sin City\n"
        "\n"
        "Sin City is an online, open-world fantasy game, driven \n"
        "by survival mechanics, random encounters, and dark twists!"
    )

""" Runs the menu. 

@return null
"""
def menu(): 
    running = True
    while running: 
        clearScreen()
        showLogo()

        print ("1) Background ")
        print ("2) Utilities ")
        print ("3) Help ")
        print ("4) Quit ")

        choice = input("\nChoose: ")

        if choice == '4': 
            return 0
        elif choice == '3': 
            help() 
        elif choice == '2': 
            utilities()
            input()
        elif choice == '1': 
            background() 
            input()
    
""" Displays project information. 

@return null
"""
def infomode(): 
    
    clearScreen() 
    menu()

""" Initialize argument parser. 

@return null
"""
def initParser(): 
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description= logo + 'Cluster Application Programming Interface',
            epilog='For more help, type __init__.py -h')
    
    '''
    Specify different interface modes
    - virtual 
    '''
    mode_group = parser.add_mutually_exclusive_group(required=True)
    
    # Guest Mode 
    mode_group.add_argument('--v', '--virtual', help='Create virtual structure.',
                            action='store_true')

    # Run Mode 
    mode_group.add_argument('--r', '--run', help='Run flask server.',
                            action='store_true')
    
    # Info Mode 
    mode_group.add_argument('--i', '--info', help='Show project information.',
                            action='store_true')
    
  
    '''
    
    parser.add_argument(
        '-un', '--username', default=['guest'], type=str, help="Specify user name.", nargs='+')
    '''
    
    return parser 

""" The main sequence. 

@return null
"""
def main(): 

    parser = initParser()
    args, unknown = parser.parse_known_args() 

    if args.v:
        scenario = Scenario() 
        scenario.virtual_init() 
    elif args.r: 
        scenario = Scenario() 
        scenario.start() 
        scenario.get_run_thread().start()
    elif args.i: 
        infomode()

""" Waits for the program to be called. 

@return null
"""
if __name__ == '__main__': 
    main() 