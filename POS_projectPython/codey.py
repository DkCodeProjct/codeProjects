
def main():
    
    jar = 12
    while True:
        getJar = Valid('1.put\n2.pick\n3.EXIT\n>.')
        if getJar == 3:
            break
       
        if getJar == 1:
            try:
                depositeCookie = int(input('put '))
                if jar == 12:
                    print('full')
                elif depositeCookie + jar > 12:
                    depositeCookie = depositeCookie+jar - 12
                    print('Excess of ',depositeCookie,'cookie ')
                
                else:
                    depositeCookie += jar
                    print(jar*'*')
            except ValueError:
                pass
               
        else:
            try:
                pickCookie = int(input('pick '))
                
                if pickCookie > jar :
                    print('notEnoughCookie')
                    print(f'{jar*"*"} cookies  left from the jar')

                else:
                    jar -= pickCookie
                    print(f'cookies {jar*"*"}')
            
            except ValueError:
                pass
    print(' >>> yummy yummy <<<')
    print('>>>               <<<')

def Valid(prompt):
    while True:
        try:
            user = int(input(prompt))
            if user in [1,2,3]:
                return user
            else:
                pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()