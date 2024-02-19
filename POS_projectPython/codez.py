import time
import csv
import datetime

def main():
    subTotal = 0 
    totalItem = []
    countItem = 0

    while True:
        print('-- Press [Enter] to Add Item.. --\n-- Press [p] To print --\n')
        user = isValid('add item >.')
        if user == '':
            countItem += 1

        if user == 'p':
            time.sleep(3) 
                
            print(f'SUB TOTAL: {subTotal}$')
         
            while True:
                getPaymnt = validFloat('Payment: ')
                print('\n')
                if getPaymnt >= subTotal:
                    change = getPaymnt - subTotal
                    time.sleep(3)
                    
                    print('------------------------------')
                    print(f'Date {datetime.date.today()}')
                    print('Cash Sales Recipt')
                    print('------------------------------')
                    print('   ==============')
                    print('   Item Name\n     Qty*    Unit Price') 
                    print('   ==============')
                    for itm in totalItem:
                       
                       # add $ sign and make print bill done and finish the project
                       
                        print(f'   {itm[0].upper()}\n     {itm[1]} * {itm[2]}     {itm[1]*itm[2]}') # get index of item in itemList;; i just did it work
                    print(f'\nNo of item = {countItem}')
                    
                    print('------------------------------')
                    print(f'SUB TOTAL   {subTotal}$')
                    print(f'cash paid   {getPaymnt}$')
                    print(f'Change      {getPaymnt - subTotal}$')
                    print('------------------------------')
                    print(' ** THANK YOU COME AGAIN **')
                    print('  dk_softwear_sol.pvt[lmt]')
                    
                    time.sleep(1.5)
                    break
                
                else:
                    print(f'Error; Need:{subTotal}')
               
            break  # break and print the bill when press p //
        
        name = validStr('Name ')

        qnt = validFloat('Qnt* ')

        price = validFloat('Unit Price ')
        
        total = qnt * price
        subTotal += total
        
        item = (name, qnt, price, total)
        totalItem.append(item)      
        listItem = (f'Name:{name}, Quantity:{qnt}, Total:{total}')
        
        with open('ItemData0.csv', 'a', newline='') as file:
            
            writer = csv.writer(file)
            headers = ['Name', 'Quantity', 'Price', 'Total']# make header on top csvFile
            
            writer.writerow([f'name:{name}, quantity:{qnt}, price:{price}, total:{total}'])
            
        
        
def validStr(prompt):
    while True:
        try:
            user = input(prompt)
            return user
        except ValueError:
            pass

def validFloat(prompt):
    while True:
        try:
            user = float(input(prompt))
            return user
        except ValueError:
            pass

def isValid(prompt):
    while True:
        try:
            user = input(prompt).lower().lstrip()
            if user == '' or user == 'p':
                return user
            else:
                print("Press[p] to print\npress[enter] to addAnotherItem")
        except ValueError:
            pass
main()