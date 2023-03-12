import os
from os import system, name 
import sys 
import argparse

from obj.scenario import Scenario 

logo = (r''' 
  _____________________________________             _______________________
 |                                     |           /                       |
 |                                     |          /                        |
 \ ____________________________________/         /                         |
                |       |                       /                          |
                |       |                      /        /------------------|
                |       |                     |        |
                |       |        |--------|   |        |
                |       |        |--------|   |        |
                |       |                      \        \------------------|
                |       |                       \                          |
                |       |                        \                         |
                |       |                         \                        |
                \ _____ /                          \ ______________________|
 -----------------------------------------------------------------------------------
|                                                                                   |
 -----------------------------------------------------------------------------------
''')

# Clear terminal screen
def clearScreen():
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

# Display project info
def infomode(): 
    
    clearScreen() 
    print(logo) 


# Init argument parser
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

# Conduct main sequence 
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

# Listen for main sequence 
if __name__ == '__main__': 
    main() 