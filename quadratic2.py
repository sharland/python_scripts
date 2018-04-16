
from tkinter import *

def __init__(self, master):
    # initialise frame
    super(Application, self).__init__(master)
    self.grid()

            

def solWin(ABCXD):
   # wn.setup(width=1075,height=620,startx=250,starty=50)
   # wn.title("Quadratic Equation Soluton")
    root.title("Quadratic Equation Solver")
    root.geometry('1075x620')
    #strABCXD=str(ABCXD) need to separate the A-D values by ,
    A=ABCXD[0]
    B=ABCXD[1]
    C=ABCXD[2]
    x1=ABCXD[3]
    x2=ABCXD[4]
    dis=ABCXD[5]
    int_A=round(A,0)
    int_A=int(int_A)
    int_B=round(B,0)
    int_B=int(int_B)
    int_C=round(C,0)
    int_C=int(int_C)
    x2x=x2

    if dis==0:
        x2x ="no X2 solution"
        int_x1=round(x1,0)
        int_x1=int(int_x1)
    elif dis >0:
        int_x2=round(x2,0)
        int_x2=int(int_x2)
        int_x1=round(x1,0)
        int_x1=int(int_x1)
    elif dis < 0:
        x2=x2
        x1=x1


    max = 130
    turtle.goto (-520,268)
    print("The discriminant is "," "+str(dis))
    turtle.goto (-520,248)
    print("The discriminant is ")
    if dis > 0:
        print("greater than 0 so there are 2 roots")
    elif dis < 0:
         print("There are no roots")
    elif dis == 0:
        print("equal to 0, there is only 1 root")

   
                

def solveA():
    try:
        A = float(inputA.get())
        B = float(inputB.get())
        C = float(inputC.get())

        dis = B*B
               
        dis = dis - 4*A*C
        discriminant.set(dis)
       

        if dis > 0:
            output.set("Greater than 0")
            x1 = -B +dis**0.5
            x2 = -B -dis**0.5
            x1 = x1/(2*A)
            x2 = x2/(2*A)
            answer1.set(x1)
            answer2.set(x2)
            solWin(ABCXD)
            return A,B,C,x1,x2,dis
        elif dis < 0:
            print("less than 0")
            B1=-B/(2*A)
            B2=(-dis)**0.5/(2*A)
            x1=str(B1)+"+"+str(B2)+"i"
            x2=str(B1)+"-"+str(B2)+"i"
            answer1.set(x1)
            answer2.set(x2)
            solWin(ABCXD)
            return A,B,C,x1,x2
        else:
            output.set("Equals 0")
            x1 = -B + dis**0.5
            x2 = -B - dis**0.5
            x1 = x1/(2*A)
            x2 = x2/(2*A)
            answer1.set(x1)
            answer2.set("There is no x2 as there is only 1 root")
            solWin(ABCXD)
            return A,B,C,x1,x2,dis
       
    except ValueError:
        pass

 #   ABCXD = solveA()
 #   solWin(ABCXD)

        
root = Tk()

root.title("Quad Solver")
root.geometry('800x400+50+20')
mainframe= Frame()
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))




inputA=StringVar()
inputB=StringVar()
inputC=StringVar()
A=float()
B=float()
C=float()
ABCXD=float()
answer = StringVar()
answer1 = StringVar()
answer2 = StringVar()
output = StringVar()
discriminant = StringVar()
x1=float()
x2=float()



Label(mainframe, text="").grid(column=1,row=1,columnspan=10,sticky=S)
Label(mainframe, text="QUAD SOLVE").grid(column=1,row=2,columnspan=6,sticky=E)
Label(mainframe, text="if you have...").grid(column=1,row=3,columnspan=10,sticky=S)
Label(mainframe, text="Just enter A,B,C below").grid(column=1,row=4,columnspan=10,sticky=S)
Label(mainframe, text="").grid(column=1,row=5,columnspan=10,sticky=S)
Label(mainframe, text="A").grid(column=2,row=5,columnspan=10,sticky=S)
Label(mainframe, text="").grid(column=3,row=5,columnspan=10)
Label(mainframe, text="").grid(column=4,row=5,columnspan=10)
Label(mainframe, text="B").grid(column=5,row=5,columnspan=10,sticky=S)
Label(mainframe, text="").grid(column=6,row=5,columnspan=10)
Label(mainframe, text="").grid(column=7,row=5,columnspan=10)
Label(mainframe, text="C").grid(column=8,row=5,columnspan=10,sticky=S)
Label(mainframe, text="").grid(column=9,row=5,columnspan=10)
Label(mainframe, text="").grid(column=10,row=5,columnspan=10)
Label(mainframe, text="").grid(column=1,row=1,columnspan=10)

Button(mainframe,text="solve",command = solveA).grid(row = 8, column = 4, sticky = (W,E))

input_entryA=Entry(mainframe,width=10,textvariable = inputA)
input_entryA.grid(column=2, row =6, sticky= E)
Label(mainframe, text="X\xb2").grid(column=3,row=6,sticky=W)
Label(mainframe, text="+").grid(column=4,row=6)
input_entryB=Entry(mainframe,width=10,textvariable = inputB)
input_entryB.grid(column=5, row =6, sticky=(E))
Label(mainframe, text="X").grid(column=6,row=6,sticky=W)
Label(mainframe, text="+").grid(column=7,row=6)
input_entryC=Entry(mainframe,width=10,textvariable = inputC)
input_entryC.grid(column=8, row =6, sticky= E)
Label(mainframe, text="=0").grid(column=9,row=6,sticky=W)
Label(mainframe, text="").grid(column=1,row=7)




root.mainloop()

                                                               






               
