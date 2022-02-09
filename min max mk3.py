print("To stop input 'q'")
list_1= []
termination = ["q"]
while True:
    insert_number=input("insert number : ")
    if insert_number not in termination:
        list_1.append(insert_number)
    else:
        pass
        break
list_2 = [s for s in list_1 if s.isdigit()]
list_2 = list(map(int, list_2))
print("The Smallest number is ",min(list_2))
print("The Largest number is",max(list_2))