import turtle 

win = turtle.Screen()
Turt = turtle.Turtle()
Turt.speed(10000000)
#####  start ###########
length  = 10

def turnred():
    #Turt.pensize(10)
    Turt.color("red")

def turnorange():
    #Turt.pensize(10)
    Turt.color("orange")

def turnyellow():
    #Turt.pensize(10)
    Turt.color("yellow")

def turngreen():
    #Turt.pensize(10)
    Turt.color("green")

def turnblue():
    #Turt.pensize(10)
    Turt.color("blue")

def turnpurple():
    #Turt.pensize(10)
    Turt.color("purple")

def turnblack():
    #Turt.pensize(10)
    Turt.color("black")



def turnwhite():
    #Turt.pensize(10)
    Turt.color("white")


def draw():
    Turt.forward(length)
    Turt.left(120)
    Turt.forward(length)
    Turt.left(120)
    Turt.forward(length)
    Turt.right(120)
    Turt.forward(length)
    Turt.left(120)
    Turt.forward(length)
    Turt.left(120)
    Turt.forward(2*length)
    Turt.left(120)
    Turt.forward(2*length)
    Turt.left(120)
    Turt.forward(length)
    Turt.left(120)
    Turt.forward(length)

win.onkey(draw,'c')
win.onkey(turnwhite,"7")
win.onkey(turnpurple,"6")
win.onkey(turnblue,"5")
win.onkey(turngreen,"4")
win.onkey(turnyellow,"3")
win.onkey(turnorange,"2")
win.onkey(turnred,"1")
win.onkey(turnblack,"0")












### end ###
win.listen()
win.mainloop()
