# from turtle import *
# colors = ['red', 'blue', 'brow', 'yellow','grey' ]

# for i in range(3,8):
#     color(colors[i-3])
#     for u in range(i):
#         forward(100)
#         left(360/i)

# mainloop()

from turtle import *
colors = ['red','blue','green', 'yellow', 'grey']
for j in range(len(colors)):
    color(colors[j])
    begin_fill()
    for i in range(4):
        fd(100)
        left(90) 
    end_fill()
    penup()
    forward(50)
    pendown()  
mainloop()