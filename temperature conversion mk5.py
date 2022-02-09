print("this program converts temps from celsius to fahrenheit and vice versa\n")
print("to convert from celsius to fahrenheit choose mode 1")
print("to convert from fahrenheit to celsius choose mode 2\n")
mode=["1","2"]
choose_mode=(input(("mode : ")))
while choose_mode not in mode:
    print("the mode you have chose doesn't exist, please choose a viable mode ")
    choose_mode=(input(("mode : ")))
while choose_mode in mode:
    if choose_mode=="1":
        while True:
            try:
                tempc=float(input("enter the temp in celsius\n"))
                tempf=(tempc*(9/5))+32
                print ("The temperature in fahrenheit is",tempf)
                break
            except ValueError:    
                print("please enter a valid temperature")      
    if choose_mode=="2":
        while True:
            try:
                tempf=float(input("enter the temp in fahrenheit\n"))
                tempc=(tempf-32)*(5/9)
                print ("The temperature in celsius is",tempc)
                break
            except ValueError:    
                print("please enter a valid temperature")
  
    break        
        
