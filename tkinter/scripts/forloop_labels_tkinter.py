import tkinter

#I've added a print command to show in the shell
#what order the for loop sets up things
root = tkinter.Tk(  )
for r in range(3):
    print("row",r)
    for c in range(4):
        print("column",c)
        tkinter.Label(root, text='R%s/C%s'%(r,c),
            borderwidth=1 ).grid(row=r,column=c)

root.mainloop(  )
