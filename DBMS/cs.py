import csv
from tabulate import tabulate

class PsycholDataBase:
     def __init__(self):
        self.currentID = 0
        self.data = []
        self.filename = "pychoDB.csv"
        self.addId()

    def addId(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data.append(row)
                self.currentID = max(self.currentID, int(row['Id']))
    
    
    def save_data(self, new_data):
        with open(self.filename, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=['Id', 'Name', 'Age', 'civilStatus', 'Deseas', 'TherapySesions'])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(new_data)

        
    def getData(self): 
# wtf i put single qute in feilds and put "" in enter data {name..} ERROR occured
        feilds = ['Id','Name','Age',"civilStatus", "Deseas",'TherapySesions']
        enterData = {
            'Id':self.currentID +1,
            'Name':input('Name '),
            'Age':input("Age "),
            "civilStatus":input('civil status '),
            "Deseas":input('Deseas '),
            "TherapySesions":input("how many thereapy sesions so far ")

        }
        
        self.currentID += 1
        self.data.extend(dict(enterData))
        with open(self.filename, 'a') as file:
            writer = csv.DictWriter(file,fieldnames=feilds)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow((enterData))
    
    def displayData(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    
    def searchData(self):
        search = input('> ')
        with open(self.filename,'r') as file:
            reader = csv.DictReader(file)
            found = False
            for row in reader:
                for key,val in row.items():
                    
                    if search in val:
                        found = True
                        print(row)
            if not found:
                print('no such a data')
            

    
    def AccessDataBase(self):
        while True:
            print('[0] Quit\n[1] Add Data To DB\n[2] Display Data in DB\n[3]Search for DB')
            try:
                choice = int(input("> "))
            
                if choice == 0:
                    break
                elif choice == 1:
                    self.getData()
                elif choice == 2:
                    self.displayData()
                else:
                    self.searchData()
            except ValueError:
                pass

def main():
    psychodb = PsycholDataBase()
    psychodb.AccessDataBase()
if __name__ == "__main__":
    main()
