import turtle
x=10
y=72
z=2
h=1
kermit = turtle.Turtle()
kermit.color("indigo")
while z<25:
    for i in range (5):
        kermit.forward(x)
        kermit.left(y)
    kermit.right(h)
    h+=2
    x+=4
    z+=1
turtle.done()