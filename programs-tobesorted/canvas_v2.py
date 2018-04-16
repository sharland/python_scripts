#http://etutorials.org/Programming/Python+tutorial/Part+III+Python+Library+and+Extension+Modules/Chapter+16.+Tkinter+GUIs/16.7+The+Canvas+Widget/
from tkinter import *
import math

root = Tk(  )

# first, a row for function entry and action button
fram = Frame(root)
Label(fram,text='f(x):').pack(side=LEFT)
func = Entry(fram)
func.pack(side=LEFT, fill=BOTH, expand=1)
butt = Button(fram, text='Plot')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

# first, a row for function entry and action button
fram2 = Frame(root)
Label(fram2,text='f(x):').pack(side=LEFT)
func2 = Entry(fram2)
func2.pack(side=LEFT, fill=BOTH, expand=1)
butt2 = Button(fram2, text='Plot')
butt2.pack(side=RIGHT)
fram2.pack(side=TOP)

# then a row to enter bounds in
fram = Frame(root)
bounds = [  ]
for label in 'minX', 'maxX', 'minY', 'maxY':
    Label(fram,text=label+':').pack(side=LEFT)
    edit = Entry(fram, width=6)
    edit.pack(side=LEFT)
    bounds.append(edit)
fram.pack(side=TOP)

# and finally the canvas
c = Canvas(root)
c.pack(side=TOP, fill=BOTH, expand=1)

def minimax(values=[0.0, 1.0, 0.0, 1.0]):
    "Adjust and display X and Y bounds"
    for i in range(4):
        edit = bounds[i]
        try: values[i] = float(edit.get(  ))
        except: pass
        edit.delete(0, END)
        edit.insert(END, '%.2f'%values[i])
    return values

def plot(  ):
    "Plot given function with given bounds"
    #minx = 0.0, maxx = 1.0 from list above, by calling function def minimax()
    minx, maxx, miny, maxy = minimax(  )

    # get and compile the function by returning the formula in the entry widget
    f = func.get(  )
    f = compile(f, f, 'eval') # converting the text formula in to values

        # get Canvas X and Y dimensions
    CX = c.winfo_width(  )
    print(CX)
    CY = c.winfo_height(  )
    print(CY)

    # compute coordinates for line
    coords = [  ]
    for i in range(0,CX,5):
        coords.append(i)
        x = minx + ((maxx-minx)*i)/CX
        y = eval(f, vars(math), {'x':x})
        j = CY-CY*(y-miny)/(maxy-miny)
        coords.append(j)
      
    # draw line
    c.delete(ALL)
    c.create_line(*coords)

def plot2(  ):
    "Plot given function with given bounds"
    #minx = 0.0, maxx = 1.0 from list above, by calling function def minimax()
    minx, maxx, miny, maxy = minimax(  )

    # get and compile the function by returning the formula in the entry widget
    f = func2.get(  )
    f = compile(f, f, 'eval') # converting the text formula in to values

        # get Canvas X and Y dimensions
    CX = c.winfo_width(  )
    CY = c.winfo_height(  )
   
    # compute coordinates for line
    coords = [  ]
    for i in range(0,CX,5):
        coords.append(i)
        x = minx + ((maxx-minx)*i)/CX
        y = eval(f, vars(math), {'x':x})
        j = CY-CY*(y-miny)/(maxy-miny)
        coords.append(j)
    

    # draw line
   # c.delete(ALL)
    c.create_line(*coords)

butt.config(command=plot)
butt2.config(command=plot2)

# give an initial sample in lieu of docs
f = 'sin(x) + cos(x)'
func.insert(END, f)
minimax([0.0, 10.0, -2.0, 2.0])

root.mainloop(  )

