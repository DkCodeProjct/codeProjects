import random
from pyfiglet import Figlet

def shoWinner(word):
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font='slant')
    txt = word
    outpu = figlet.renderText(text=txt)
    return outpu



def checkList(xyz):
    for i in range(1, len(xyz)):
        if xyz[i] < xyz[i-1]:
            return False
    return True

def genCompNum(last):
    genNumList = []
    genNum = random.randint(1,7)
    stop = last + genNum

    for i in range(last, stop):
        if i != last:
            genNumList.append(i)
    return genNumList


last = 0
xyz = []
choice = input("f-> 1. s-> 2. :")
while last != 21:

    if choice == 'f':
    
        print("user 1 inupt,")
        print("how many num you wish to input ")
        usr1 = int(input("> "))
        if usr1 in range(1,7):
            print("enter values")
            for _ in range(usr1):
                
                usr1Nums = input(">")
                usr1Nums = int(usr1Nums)
                xyz.append(usr1Nums)
            last = xyz[-1]
            print("order of input after user")
            print(xyz)
            if last == 21:
                print(shoWinner('User Win'))
                print('win')
            if checkList(xyz) == False:
                print('order not in consecutive order')
                print(shoWinner('Computer Win'))
                exit(0)
            
        
            comp = last
            genNums = genCompNum(comp)
            
            xyz.extend(genNums)
            print("order of the input after computer ")
            print(xyz)
    else:

        comp = last
        genNums = genCompNum(comp)
        
        xyz.extend(genNums)
        print("order of the input after computer ")
        print(xyz)
        
        print("user 1 inupt,")
        print("how many num you wish to input ")
        
        usr1 = int(input("> "))
        if usr1 in range(1,7):
            print("enter values")
            for _ in range(usr1):
                
                usr1Nums = input(">")
                usr1Nums = int(usr1Nums)
                xyz.append(usr1Nums)
            last = xyz[-1]
            print("order of input after user")
            print(xyz)
            if last == 21:
                print(shoWinner('User Win'))
                print('win')
            if checkList(xyz) == False:
                print('order not in consecutive order')
                print(shoWinner('Computer Win'))
                exit(0)

