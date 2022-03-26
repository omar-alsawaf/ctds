import random
list_1=["t","w","m"]
a=0
b=0
while not (a==2 or b==2):
    u=input("user : ").lower()
    if u not in list_1:
        print("you chose a non viable option")
        continue
    c=random.choice(list_1)
    print("computer choice is",c)
    if u=="t" and c=="w":
        b=b+1
        continue
    elif u=="t" and c=="m":
        a=a+1
        continue
    elif u=="t" and c=="t":
        continue
    elif u=="w" and c=="t":
        a=a+1
        continue
    elif u=="w" and c=="w":
        continue
    elif u=="w" and c=="m":
        b=b+1      
        continue
    elif u=="m" and c=="t":
        b=b+1
        continue
    elif u=="m" and c=="m":
        continue
    elif u=="m" and c=="w":
        a=a+1
        continue
if a==2:
    print("user won")
elif b==2:
    print("computer won")