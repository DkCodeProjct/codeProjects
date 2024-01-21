import random

print('<--RockPaperScissor-->')

print('winningRulesOfTheGame:\nrock vs paper ->~paper~\npaper vs scissor -> ~scissor\n scissor vs rock -> ~rock~\n')
print('CHOICES:\n1. rock,\n2. paper,\n3.scissor\n\n')

while True:
    user = int(input('input: '))
        

    if user == 1:
        userChoice = 'Rock'
    elif user == 2:
        userChoice = 'Paper'
    else:
        userChoice = 'Scissor'



    compChoces = [1,2,3]
    compChoice = random.choice(compChoces)

    if compChoice == 1:
        comp = 'rocK'
    elif compChoice == 2:
        comp = 'papeR'
    else:
        comp = 'scissoR'

    if user == 1 and compChoice == 1:
        print('--Its a tie--')
        print(f'userChoice: {userChoice}\ncomputerChoice: {comp}')

    if user == 1 and compChoice == 2:
        print('computerWin')
        print(f'userChoice: {userChoice}\ncomputerChoice: {comp}')

    if user == 2 and compChoice == 1:
        print('youWin')
        print(f'userChoice: {userChoice}\ncomputerChoice: {comp}')

    if user == 3 and compChoice == 2:
        print('youWin')
        print(f'userChoice: {userChoice}\ncomputerChoice: {comp}')

    if user == 2 and compChoice == 3:
        print('computerWin')
        print(f'userChoice: {userChoice}\ncomputerChoice: {comp}')

    if user == 3 and compChoice == 1:
        print('ComputerWin')
        print(f'userChoice: {userChoice}\ncomputerChoice: {comp}')

    if user == 1 and compChoice == 3:
        print('userWin')
        print(f'userChoice: {userChoice}\ncomputerChoice: {comp}')


    doMore = input('doMore: [y,n]').lower()
    if doMore == 'n':
        break

print('thankYou')





    
    
    



