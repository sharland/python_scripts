import pyglet

window = pyglet.window.Window() #default window constructor

label = pyglet.text.Label('Hello world',
                          font_name='Calibri',
                          font_size=36,
                          x=window.width//2,y=window.height//2,
                          anchor_x='center',
                          anchor_y='center')

@window.event #this is dispatched to the window to give it a chance to clear its contents and run
def on_draw():
    window.clear()
    label.draw()


pyglet.app.run() 
