import random
import cv2
import os

baga=10
bagb=10
bagc=10
list1=[baga,bagb,bagc]

def win():
    img=cv2.imread('K:\Pictures\Saved Pictures\win.jpg',1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyallwindows()

def lost():
    img=cv2.imread('K:\Pictures\Saved Pictures\lost.jpg',1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyallwindows()

def bag():
    while True:
        try:
            i=int(input("please enter the number of bag you want 1,2 or 3 : "))
            if (list1[i-1]>0):
                return i;
            else:
                print("this bag is empty")
                continue
        except ValueError:
            print("please enter a number")
            continue
        except IndexError:
            print("please enter a bag that exists")
            continue

def balls():
    try:
        x=int(input('plz enter the no of balls you want to remove : '))
    except ValueError:
        x=int(input('plz enter the no of balls you want to remove : '))
    return x;

def computer():
    while True:
        h=random.randint(0,2)
        if (list1[h]>0):
            return h;
        else:
            continue

while not (list1[0]==0 and list1[1]==0 and list1[2]==0):
    c=(int(bag())-1)
    x=int(balls())
    while not(x>0 and x<=5):
        print("please enter a number between 0 and 5")
        x=int(balls())
    while (x>0 and x<=5):            
        while not (list1[c]-x>=0):
            print("bag doesnt have this number of balls")
            x=int(balls())
        while (list1[c]-x>=0):
            list1[c]-=x
            if(list1[0]==0 and list1[1]==0 and list1[2]==0):
                win()
                break
            z=computer()
            if (list1[z]>=5):
                kilo=random.randint(1,5)
            elif(list1[z]>1 and list1[z],5):
                kilo=random.randint(1,z)
            else:
                kilo=1
            list1[z]-=kilo
            if(list1[0]==0 and list1[1]==0 and list1[2]==0):
                print("you lost")
                break
            print("bag1=",list1[0])
            print("bag2=",list1[1])
            print("bag3=",list1[2])
            break
        break