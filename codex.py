from tabulate import tabulate
import sys
import csv

print("enter your details below:")
inputUser = input("name:\n>.. ")

askAge = int(input("age:\n>.. "))
if askAge > 18:
    askRelationship = input("relationship:[y/n]\n>.. ").lower()
    if askRelationship == 'y':
        askHowLong = input("how long:\n>.. ")
    else:
        askWhy = input("reason for not having one:\n>.. ")
    emplymentStatus = input("do you have a job[y/n]\n>.. ").lower()
    if emplymentStatus == 'n':
        askWhy = input("why:\n>.. ")
    else:
        askSalary = int(input("salary:\n>.. "))
        if askSalary > 125000:
            askTax = input("do you pay tax:[t/n\n>.. ").lower()
            if askTax == 'y':
                askHowLong = input("how long:\n>.. ")
            else:
                print("why:\n>.. ")
        else:
            askJob = input("whats you'r job:\n.. ")
            jobPost = input("you'r post:\n>.. ")
    with open('student.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['relationship','emplyment','salary','taxation','jobpost'])
        writer.writerow({'relationship':askRelationship, "emplyment":emplymentStatus})

print("not allowed...!")
exit(0)






