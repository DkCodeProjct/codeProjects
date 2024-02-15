# // import math 
# // import pandas as pd
# // from pyfiglet import Figlet
import time

def add(x,y):
    return (x + y)

def sub(x,y):
    return (x - y)

def mul(x,y):
    return (x * y)

def div(x,y):
    return (x / y)

def rem(x,y):
    return (x % y)

def pow(x,y):
    return (x ** y)
def main():   
    while True:
        chooseCal = chooseCalOp('ExiT[3]\nnormalCal[1]\nsci-cal[2]\n>.')
        if chooseCal == 1:
            getNormalOp = getOpNum('00. ExiT[0]\n01.add\n02.sub\n03mul')
            if getNormalOp == 0:
                print('-----')
                break
            x = validInt('x ')
            y = validInt('y ')

            if getNormalOp == 1:
                print(f'{x} + {y} = {add(x,y)}')
                time.sleep(2)
            elif getNormalOp == 2:
                print(f'{x} - {y} = {sub(x,y)}')
                time.sleep(2)
            else:
                
                print(f'{x} + {y} = {mul(x,y)}')
                time.sleep(2)

        elif chooseCal == 2:
            while True:
                getSciOp = getOpNum('00. ExiT[0]\n01.div\n02remander\n03.pow')
                
                if getSciOp == 0:
                    print('-----')
                    break
                z = validInt('x ')
                w = validInt('y ')

                if getSciOp == 1:
                    print(f'{z} / {w} = {div(z,w)}')
                    time.sleep(2)
                elif getSciOp == 2:
                    print(f'{z} % {w} = {rem(z,w)}' )
                    time.sleep(2)
                else:
                    print(f'{z} ** {w} = {pow(z,w)}')
                    time.sleep(2)
        else:
            print('-----')
            break

def chooseCalOp(promptUser):
    while True:
        try:
            user = int(input(promptUser))
            if user in [1, 2, 3]:
                return  user
            else:
                print("wasn't in [1/2/3]")
        except ValueError:
            pass

def validInt(promptUser):
    while True:
        try:
            user = int(input(promptUser))
            return user
        except (ValueError,ZeroDivisionError):
            pass
def getOpNum(userInput):
    while True:
        try:
            user = int(input(userInput))
            if user in [0,1,2,3]:
                return user
            else:
                print("wasn't in [0/1/2/3]")
        except ValueError:
            pass

if __name__ == '__main__': # testCODE || down here
    main()

"""
from project import chooseCalOp
import pytest

def testChooseCalOp():
    assert chooseCalOp(3) == True
    assert chooseCalOp(2) == True
    assert chooseCalOp(1) == True

def Char_test():
    assert chooseCalOp('cat') == False

def invlaid_test():
    assert chooseCalOp(4) == False
"""