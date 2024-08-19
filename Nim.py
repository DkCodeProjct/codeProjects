# : Making the nim game
# : rulse-
#         | take nums untill piles are empty  


"""
    uh,, i wrote some childish code,, for Nim game,,
    i remember i wrote code way before for hangman like game 
    and that code i use this stratagy which code user play 1 
    and computer paly 1,, since i dont know how to togle between and 
    give chance to paly user and com, i use this stratagy i used before

    its very uneficent...
    but at the end of the day i got the job done.

    NOW I CAN seaech Internet and look How others Write the 
    Nim game Eficently and Cleanly More Than Me...
    And Learn From it
    
"""
import random

piles = [1, 3, 5, 7]

lastRmUsr = 0
lasrRmCom = 0
def rmCom(pile):
    while True:
        pileNum = random.randint(0, 3)
        if pile[pileNum] > 0:
            rmNum = random.randint(1, pile[pileNum])
            pile[pileNum] -= rmNum
            
            print(f'comp rm: from pile {pileNum + 1},, {rmNum} nums')
            break
    return pile

choosePlay = int(input('Play: '))
while True:
    if choosePlay == 1:
        userPile = int(input('choose pileNum:[0/1/2/3] ')) 
        userRmNum = int(input('how many num to rm: '))
        
        
        if piles[userPile] > 0:
            piles[userPile] -= userRmNum
            lastRmUsr += 1
        else:
            print('<0,, cant rm')
        print(f'user rm: from pile {userPile},, {userRmNum} nums')
        print(piles)

        print('compTurn')

        print(rmCom(piles))
        lasrRmCom += 1
    
    
    else:
        print(rmCom(piles))
        lasrRmCom += 1
        
        
        print('userturn')

        userPile = int(input('choose pileNum:[0/1/2/3] ')) 
        userRmNum = int(input('how many num to rm: '))
        if piles[userPile] > 0:
            piles[userPile] -= userRmNum
            print(piles)
            lastRmUsr += 1
        else:
            print('>0,, cant rm')
        print(f'user rm: from pile {userPile},, {userRmNum} nums')
    
    
    if (all(pile==0 for pile in piles)):
        print('over')
        if lastRmUsr > lasrRmCom:
            print('computer win')
        else:
            print('user win')
        break