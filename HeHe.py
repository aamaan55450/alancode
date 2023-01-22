import turtle 

win = turtle.Screen()
win.bgcolor("black")
Turt = turtle.Turtle()
Turt.speed(10000000000)
#####  start ###########
for i in range(100000):
    Turt.circle(100)
    Turt.left(35)
    Turt.forward(10)
    if i%7 ==0:
        Turt.color("white")
    elif i%7 ==1:
        Turt.color("red")
    elif i%7 ==2:
        Turt.color("orange")
    elif i%7 ==3:
        Turt.color("yellow")
    elif i%7 ==4:
        Turt.color("green")  
    elif i%7 ==5:
        Turt.color("blue")
    elif i%7 ==6:
        Turt.color("purple")
### end ###
win.mainloop()