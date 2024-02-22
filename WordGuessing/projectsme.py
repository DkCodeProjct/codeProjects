import random

def displayWord(word,guessedChar):
    display = ''

    for char in word:
        if char in guessedChar:
            display += char
        else:
            display += '_'
    return display

def main():
    tecxtEditor = ['vim','emasc','vscode','vs','neovim','zed','notepad']
    word0 = random.choice(tecxtEditor)
    linux = ['kali','fedora','arch','ubuntu','mint','redhat','debian']
    word1 = random.choice(linux)
    choose = int(input('-choose Words-\nLinux -> [1]\nText Editors -> [2]\n[1/2] : '))
    word = ''
    if choose == 1:
        word = word0
    else:
        word = word1


    attempts = int(input('howManyAttempts: '))

    guessedChar = []

    while attempts != 0:
        currentGame = displayWord(word, guessedChar)
        print('Game: ',currentGame)

        getChar = input('char: ')

        if getChar in guessedChar:
            print('already Guessed')
            continue
        guessedChar.append(getChar)

        if getChar not in word:
            attempts -= 1
            print('Wrong')
        if '_' not in displayWord(word, guessedChar):
            print('win, ',word)
            break
    if attempts == 0:
        print('will, get him next time,', word)
main()