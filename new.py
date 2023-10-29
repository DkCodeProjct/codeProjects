def main():
    try:
        user_find = input("Find_birthYear/Age_ \nEnter:=(BY/A)").lower()
    
    except ValueError:
        pass
    
    else:
        if user_find == 'by':
            user_findyear()
        elif user_find == 'a':
            user_findAge()
        else:
            print("invalid input")

            

def user_findyear():
    try:
        currentAge = int(input("enter_age: "))
    except ValueError:
        pass
    else:
        result = 2023 - currentAge
        print(f"your birth year was {result}.")

def user_findAge():
    try:
        birthYear = int(input("enter_birth year: "))
    except ValueError:
        pass
    else:
        result_1 = 2023 - birthYear
        print(f"you'r age is {result_1}.")

if __name__ == "__main__":
    main()
