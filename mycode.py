    
totalCost = 0


while True:
    print('PleaseEnter: ----> [done:00] to quit  //\n')
    getCost = input('costs: ENTER--->[Name:Cost] ')
    
    name, cost = getCost.split(':')
    
    try:
        newName = str(name)
    except ValueError:
        pass
    
    try:
        newCost = int(cost)
    except ValueError:
        pass
    
    else:
        totalCost += newCost
    
    if getCost== 'done:00':
        askProfit = input("Do You Want to check The PROFIT:[y/n] ")
        if askProfit == 'y':
            geTpofit = int(input('enterProfit: '))
            companyProfit = totalCost - geTpofit
            print(f'Your Profit Is ---->{totalCost}-{geTpofit} == {companyProfit}')
            
            break
        
        else:
            print('TotalCost',totalCost)
            break
print("------")
    