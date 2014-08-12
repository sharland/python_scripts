import turtle
wn = turtle.Screen()

def setup(col, x, y, w, s, shape): 
    turtle.up()
    turtle.goto(x,y)
    turtle.width(w)
    turtle.turtlesize(s)
    turtle.color(col)
    turtle.shape(shape)
    turtle.down()
    wn.onkey(up, "Up")
    wn.onkey(left, "Left")
    wn.onkey(right, "Right")
    wn.onkey(back, "Down")
    wn.onkey(quitTurtles, "Escape")
    wn.listen()
    wn.mainloop()
    
#Event handlers
def up():
    turtle.fd(45)

def left():
    turtle.lt(45)

def right():
    turtle.rt(45)

def back():
    turtle.bk(45)
 
def quitTurtles():
    wn.bye()
    
setup("blue",-200,200,2,2,"turtle")

mainloop()