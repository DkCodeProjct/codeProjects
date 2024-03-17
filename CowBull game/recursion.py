import random

""" THE GAME """
#Secret Code: randomlyGenNum // password

#Guess: 1234
#Response: 0 bulls, 1 cow
#Guess: 5678
#Response: 1 bull, 2 cows

class CowBullGame:
    def __init__(self):
        self.attmpts = 5
        
    def getLevel(self):
        while True:
            try:
                print('choose Levle')
                level = int(input('level[2/3/4] '))
                if level in [2,3,4]:
                    return level
                else:
                    print('not valid')
            except ValueError:
                pass
    
    def Game(self):
        level = self.getLevel()
        
        if level == 2:
            num2 = random.randint(10,100)
            password = num2
            

        elif level == 3:
            num3 = random.randint(100,1000)
            password = num3
        else:
            num4 = random.randint(1000,10000)
            password = num4
        
        while self.attmpts != 0:
            get = input('Guess: ')
            cow = 0
            bull = 0
            for index, char in enumerate(str(password)):
                if char == get[index]:
                    cow += 1
                else:
                    bull += 1
            print(f'Cow:{cow}, Bull:{bull}')
            self.attmpts -= 1
        if self.attmpts == 0:
            print("will get'em next time")
            print(f'password: {password}')

if __name__ == "__main__":
    game = CowBullGame()
    game.Game()