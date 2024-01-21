import random

def main():
    print('<--RockPaperScissor-->')

    print('winningRulesOfTheGame:\n\nrock vs paper -> ~paper~\npaper vs scissor -> ~scissor\n scissor vs rock -> ~rock~\n')
    
    print('CHOICES:\n1. rock,\n2. paper,\n3.scissor\n\n')

    while True:
        user = verifiedInput('input: ')
            

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
            print('--Its a tie--\n')
            
            print(f'userChoice: {userChoice}\ncomputerChoice: {comp}\n')

        if user == 1 and compChoice == 2:
            print('computerWin')
            
            print(f'userChoice: {userChoice}\ncomputerChoice: {comp}\n')

        if user == 2 and compChoice == 1:
            print('youWin')
            
            print(f'userChoice: {userChoice}\ncomputerChoice: {comp}\n')

        if user == 3 and compChoice == 2:
            print('youWin')
            
            print(f'userChoice: {userChoice}\ncomputerChoice: {comp}\n')

        if user == 2 and compChoice == 3:
            print('computerWin')
            
            print(f'userChoice: {userChoice}\ncomputerChoice: {comp}\n')

        if user == 3 and compChoice == 1:
            print('ComputerWin')
            
            print(f'userChoice: {userChoice}\ncomputerChoice: {comp}\n')

        if user == 1 and compChoice == 3:
            print('userWin')
            
            print(f'userChoice: {userChoice}\ncomputerChoice: {comp}\n')


        doMore = verifiedStrInput('doMore: [y,n]')
        if doMore == 'n':
            break

    print('thankYou')


def verifiedInput(prompt):
    while True:
        try:
            user = int(input("pick_A_Choice: "))
            if user in [1,2,3]:
                return user
            else:
                print("---invlaidInput---")
        except ValueError:
            pass

def verifiedStrInput(prompt):
    while True:
        try:
            user1 = input(prompt).lower()
            if user1 == 'y' or user1 == 'n':
                return user1
            else:
                print("----InvlaidInput----")
        except ValueError:
            pass
if __name__ == "__main__":
    main()



        
        
        



