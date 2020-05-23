from turtle import *
shape("turtle")
speed(-1)
shape=int(input("enter number of edge :"))
angle = 360/shape
for i in range(shape):
    forward(100)
    left(angle)
mainloop()
