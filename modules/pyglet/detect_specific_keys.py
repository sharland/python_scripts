from pyglet.window import Window
from pyglet.window import key
from pyglet import app


window = Window()

@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.A:
        print("A was pressed")
    elif symbol == key.LEFT:
        print("left key pressed")
    elif symbol == key.ENTER:
        print("enter key pressed")

@window.event
def on_draw():
    window.clear()

app.run()

