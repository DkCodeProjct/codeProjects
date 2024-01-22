
import re

def main():
    getEmail = input("email: ")
    if verifiedEmail(getEmail):
        ipvAd = input("enterIpvAdress//[#.#.#.#]: ")
        parts = ipvAd.split(".")
    
        if len(parts) != 4:
            print("invalid ipv adress...")
        
        else:
            
            try:
                newx,newz,newy,newk = map(int, parts)
                if isvalid(newx,newy,newz,newk):
                    getName = input("name: ")
                    
                    if getName == 'joshua':
                        solveMath = int(input("2 + (2 - (2*4%3))\nanswer: "))
                        
                        if solveMath == 2 + (2 - (2*4%3)):
                            print("passWord:= 'joshua' ")
                        
                        else:
                            exit(0)
                    
                    else:
                        print("Un Othorized Name//")
                
                else:
                    print("invlaid ipv")
            
            except ValueError:
                pass
   
    else:
        print("invalid Email")            

def isvalid(newx,newy,newz,newk):
    
    if newx <= 255 and newy <= 255 and newz <= 255 and newk <= 255:
        return True
    else:
        return False
    
def verifiedEmail(Email):
    
    if re.search(r"^[^@]+@[^@]+\.(dead|hack|me|fk)$", Email):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

