

password = '1234'

attmpt = 5
while attmpt != 0:
    cow = 0
    bull = 0
    
    get = input("> ")
    for index, char  in enumerate(str(password)):
        if char == get[index]:  #use [] to index str
            cow += 1
        else:
            bull += 1
    print(f'cow {cow}, bull {bull}')
    attmpt -= 1
    if get == password:
        break
else:
    attmpt == 0
    print("game over")
    print('num, ',password)

""" THE GAME """
#Secret Code: 3768

#Guess: 1234
#Response: 0 bulls, 1 cow
#Guess: 5678
#Response: 1 bull, 2 cows