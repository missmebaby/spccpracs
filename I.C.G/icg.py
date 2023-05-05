while(True):
    print("MENU - \n 1: ASSIGNMENT \n 2: ARITHMETIC \n 3: RELATIONAL \n 4: EXIT")
    print("ENTER YOUR CHOICE : ")
    code = int(input())


    if code == 1:
        print("ENTER ASSIGNMENT EQUATION : ")
        str = input()
        str_ls = str.split('=')
        a = str_ls[0]
        b = str_ls[1]
        print(f"temp = {a}")
        print(f"{b} = temp")


    elif code == 2:
        print("ENTER ARITHMETIC EQUATION : ")
        str = input()
        first = str[:3]
        second = str[3:]
        print(f"temp = {first}")
        print(f"temp1 = temp{second}")
        
    elif code == 3:
        print("ENTER RELATIONAL EQUATION : ")


        str = input()
        
        str_ls = str.split(' ')
        a = str[:1]
        op = str[1:3]
        b = str[3:]


        address = 1000


        print(f"CURRENT ADDRESS : {address} \n IF {a}{op}{b} GOTO {address+3}")
        address = address + 1


        print(f"CURRENT ADDRESS : {address} \n T=0")
        address = address + 1


        print(f"CURRENT ADDRESS : {address} \n GOTO {address+2}")
        address = address + 1


        print(f"CURRENT ADDRESS : {address} \n T=1")
    else:
        break
        
