import turtle
import random
win = turtle.Screen()
gag = turtle.Turtle()
Turt = turtle.Turtle()
Turt.speed(5)
gag.speed(5)
win.addshape('Leopard_2_A5_der_Bundeswehr (1).gif')
win.addshape('6f045d33b0df0a2044da157778b501862.gif')
Turt.shape('Leopard_2_A5_der_Bundeswehr (1).gif')
gag.shape('6f045d33b0df0a2044da157778b501862.gif')
Turt.penup()
gag.penup()
Turt.goto(-400,0)
gag.goto(400,0)
#############################start#################################
def Turtjump():
    Turt.seth(90)
    Turt.penup()
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    Turt.goto(x,y)
    Turt.forward(100)
    Turt.backward(100)
    win.ontimer(Turtjump,1000)

def gagjump():
    gag.seth(90)
    gag.penup()
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    gag.goto(x,y)
    gag.forward(100)
    gag.backward(100)
    win.ontimer(gagjump,1000)




















































































































win.ontimer(Turtjump,1000)
win.ontimer(gagjump,1000)
##########################end##########################
win.listen()
win.mainloop()