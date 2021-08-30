import turtle

    
turtle.setup(800, 600)      # set the window size to 800 by 600 pixels
wn = turtle.Screen()        # set wn to the window object
wn.bgcolor("lightgreen")    # set the window background color
turtle.home()
x = 0
y = x*2+1

turtle.pendown
turtle.setpos(x,y)
for x in range(10,20,1):
    y = (x**2)+2*x+1
    print(turtle.pos()) # checking maths calculations
    turtle.goto(x,y)
wn.exitonclick()
    
    
