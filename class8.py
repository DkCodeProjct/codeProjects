import sys
import csv

def main():
    subTotal = 0
    items = []
    print('Press [EnterToAddItems]\npress [p] to print\n')

    while True:
       
        name = validStr('name ')
        
        quntity = validFloat('qumtity ')
        
        price =  validFloat('price ')
        
        total = quntity * price
        
        subTotal += total
        item = (name, quntity, price, total)
        items.append(item)      
        listItem = (f'Name:{name}, Quantity:{quntity}, Total:{total}')
        
        with open('itemData.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f'name:{name}, quantity:{quntity}, price:{price}, total:{total}'])
        
        printBill = isValid('>.')
        if printBill == '':
            print('Items ',listItem)
            continue
        
        if printBill == 'p':
            for item in items:
                print(item)
            print('subtotal',subTotal)
            break
def validStr(prompt):
    while True:
        try:
            user = input(prompt)
            return user
        except ValueError:
            print('invlaid')
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
            user = input(prompt)
            if user == '' or user == 'p':
                return user
            else:
                print("Press[p] to print\npress[enter] to addAnotherItem")
        except ValueError:
            pass
main()