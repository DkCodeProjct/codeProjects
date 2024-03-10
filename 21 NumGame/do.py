import random
from pyfiglet import Figlet

class Number_21:

    def __init__(self):
        
        self.last = 0
        self.xyz = []
        
    
    def check(self,xyz):
        
        for i in range(1, len(xyz)): # take the 1st num to iterate trough values 
            
            if xyz[i] < xyz[i-1]: # check if nums in the *Consecutive order
               
                return False #return False if not
        
        return True # if in the consecutive order return True
    
    
    def printWinLoose(self, word):

        figlet = Figlet() # gen the winning or loosing with slant asci code
        figlet.getFonts()
        figlet.setFont(font='slant')
        txt = word
        output = figlet.renderText(text=txt)
        return output
    
    
    def genCompNumList(self,last): 

        """so Fucking Proud im come up with this func without help of net """

        compNumsList = []
        start = last
        
        randomRange = random.randint(1, 7) #range to gen nums
        
        stop = start + randomRange # start gen by last element 
        for i in range(start, stop): #for srart and stop range gen num 
            
            if i != start: # dont print start(last element that already in list) element
                compNumsList.append(i)
        return compNumsList
    
    
    def userPlayFirst(self):
        print("how many num you wish to inptu")

        user1 = int(input(">"))
        for i in range(user1):
            valuse = input(">")
            valuse = int(valuse)
            self.xyz.append(valuse)
        self.last = self.xyz[-1]
        print("order of the input aster user inputs")
        print(self.xyz)

        compTurn = self.genCompNumList(self.last)
        self.xyz.extend(compTurn)
        self.last = self.xyz[-1]
        
        print('order of the num list after computer input')
        print(self.xyz)
    
    def userPlaySecond(self):
        while self.last != 21:
            compTurn = self.genCompNumList(self.last)
            self.xyz.extend(compTurn)
            self.last = self.xyz[-1]
            if self.last == 21:
                self.printWinLoose('computer wins')
            
            print('order of the num list after computer input')
            print(self.xyz)

            print("how many num you wish to inptu")

            user1 = int(input(">"))
            print("Enter valuse")
            for i in range(user1):
                valuse = input(">")
                valuse = int(valuse)
                self.xyz.append(valuse)
            self.last = self.xyz[-1]
            print("order of the input aster user inputs")
            print(self.xyz)
            if self.last == 21:
                self.printWinLoose("You win")
            if self.check(self.xyz) == False:
                print("order of input not in the consecutive order")
                self.printWinLoose("computer win")
                exit(0)
                 


    def StartGame(self):
        while self.last != 21:
            print('press [f] to play first')
            print('press [s] to play second')
            choice = input(".>")
            if choice == 'f':
                self.userPlayFirst()
            else:
                self.userPlaySecond()

game = Number_21()
game.StartGame()


       