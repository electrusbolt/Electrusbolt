# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:53:31 2019

@author: Osciel
"""

import math
import random
import shlex

def check_argument(args):
    if (len(args)>0) and (args[0].isdigit() == True) and (int(args[0]) > 0):
        return int(args[0])
    else:
        return -1


### place your code below this line ###

str_msg = '''
Dice Simulation Commands

1) Dice number from (2 to 5) for simulation, i.e., Dice 5
2) Confirm number of dice used in simulation, i.e., Confirm  
3) Roll simulation dice a number of times, i.e., Roll 10
4) Report the simulation results, i.e., Report
5) Help Menu, i.e., Help
6) Quit menu, i.e., Quit 

Enter command (Dice N, Confirm, Roll N, Report, Quit) below:'''

print(str_msg)


a = 1
sum = 0
### place your code above this line ###


while True:
    try:
        cmd, *args = shlex.split(input('> '))
        if len(args) == 0:
            args = []
    except ValueError:
        cmd = -1
        
    console_argument = check_argument(args)


### Place your code below this line ### 
    
    if cmd.lower() == 'dice'.lower():
        dice = console_argument
        if(6 > dice > 1):
            print('You have selected',dice, 'dice')
        else:
            print('Error: your roll must be between 2 and 5!')
    
    
    elif cmd.lower() == 'confirm'.lower():
        print('Your simulation is now using',dice, 'dice')
        
                
    elif cmd.lower() == 'roll'.lower(): 
        dice2 = console_argument
        if (dice2 > 0):
            print('You have selected to Roll', dice2)
        else:
            print('Error: your roll must be higher than 0!')

    
    elif cmd.lower() == 'report'.lower():
        for x in range(dice2):
            roll = (random.randint(1,6))
            sum1 = sum + roll
        
        while a == dice:
            a =+1
        numbers = x + dice 
        print('run:', a,'; sum:', sum1, '; dice:', dice2)
    
    elif cmd.lower() == 'help'.lower():
        print(str_msg)
    
    elif cmd.lower() == 'quit'.lower():
        print('Thank you for playing!')
        break
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    