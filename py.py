import turtle 

win = turtle.Screen()
win.addshape('Leopard_2_A5_der_Bundeswehr (1).gif')
Turt = turtle.Turtle()
Turt.speed(1)
Turt.pensize(10)


#####  start ###########
def goforward():
    Turt.forward(50)



def turnleft():
    Turt.left(90)
    Turt.forward(0)

def turnright():
    Turt.right(90)
    Turt.forward(0)

def turnbackward():
    Turt.left(180)

def turnred():
    Turt.pensize(10)
    Turt.color("red")

def turnorange():
    Turt.pensize(10)
    Turt.color("orange")

def turnyellow():
    Turt.pensize(10)
    Turt.color("yellow")

def turngreen():
    Turt.pensize(10)
    Turt.color("green")

def turnblue():
    Turt.pensize(10)
    Turt.color("blue")

def turnpurple():
    Turt.pensize(10)
    Turt.color("purple")

def turnblack():
    Turt.pensize(10)
    Turt.color("black")


def movetocursor(x,y):
    Turt.goto(x,y)

def turnwhite():
    Turt.pensize(10)
    Turt.color("white")

def makecircle():
    Turt.circle(50)

def slightlyturnright():
    Turt.right(1)
    Turt.forward(0)

def slightlyturnleft():
    Turt.left(1)
    Turt.forward(0)






    

win.onkey(slightlyturnright,"D")
win.onkey(slightlyturnleft,"A")
win.onkey(makecircle,"c")
win.onclick(movetocursor)
win.onkey(turnwhite,"7")
Turt.ondrag(movetocursor)
win.onkey(turnpurple,"6")
win.onkey(turnblue,"5")
win.onkey(turngreen,"4")
win.onkey(turnyellow,"3")
win.onkey(turnorange,"2")
win.onkey(turnred,"1")
win.onkey(turnblack,"0")
win.onkey(goforward,"w")
win.onkey(turnright,"d")
win.onkey(turnbackward,"s")
win.onkey(turnleft,"a")
### end ###
win.listen()
win.mainloop()