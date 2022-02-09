list_1=[7,8,9,88,541]
h="enter"
l="remove"
z="stop"
print('type"enter"to add a number')
print('type"remove" to remove a number')
print('type"stop" to quit')
while True:
    print(list_1)
    a=input("user : ").lower()
    if a==h:
        num=input("user : ")
        while not num.isdigit():
            print("you have to enter a number")
            num=input("user : ")      
        else:
            num=int(num)
            list_1.append(num)
            continue    
    elif a==l:
        if len(list_1)<=5:
            print("the bag has to have at least 5 numbers")   
        else:
            num=input("user : ")
            while not num.isdigit():
                print("you have to enter an integer") 
                num=input("user : ")
            else:
                num=int(num)
                if num not in list_1:
                    print("this number is not in the list")
                    continue
                else:
                    list_1.remove(num)  
    elif a==z:
        quit()
    else:
        print("enter a valid function")
        continue