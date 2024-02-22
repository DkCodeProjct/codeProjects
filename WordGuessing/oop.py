import random
from pyfiglet import Figlet
class GuessTheWord:
    def __init__(self):
        self.attempts = 3
        self.guessedChar = []
        
        self.textEditors = ['vim','emasc','vscode','vs','neovim','zed','notepad']
        
        self.linux = ['kali','fedora','arch','ubuntu','mint','redhat','debian']
    
    def printWin(self,word):
        figlet = Figlet()
        figlet.getFonts()
        figlet.setFont(font='slant')
        txt = word
        win = figlet.renderText(txt)
        print(win)
    
    def displayWord(self, word, guessedChar):
        display = ''
        for char in word:
            if char in guessedChar:
                display += char
            else:
                display += '_'
        return display
    
    def Game(self):
        txtEditor = random.choice(self.textEditors)
        linx = random.choice(self.linux)
        choose = int(input('| -choose Words- |\nLinux -> [1]\nText Editors -> [2]\n[1/2] : '))
        
        word = ''
        if choose == 1:
            word = linx
        else:
            word = txtEditor

        while self.attempts != 0:
            chooseWord = self.displayWord(word, self.guessedChar)
            print('-WORD- ',chooseWord)

            getChar = input('char ')

            if getChar in self.guessedChar:
                print("already Guessed...")
            self.guessedChar.append(getChar)

            if getChar not in word:
                self.attempts -= 1
                print('-Wrong-')
                
            if '_' not in self.displayWord(word, self.guessedChar):
                self.printWin('WIN')
                
                break
        if self.attempts == 0:
            print(f"will got'em next time\nThe Word was ->\n{self.printWin('LOOSE')} ",word)

def main():
    guess = GuessTheWord()
    guess.Game()

if __name__ == "__main__":
    main()