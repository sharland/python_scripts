# bingo.py - based on specimen task (WJEC)
# code by Mark Tranter - http://community.computingatschool.org.uk/resources/222

from tkinter import *
from random import shuffle

def get_number(n, lbl, btn,*ignore):
        """When the button is clicked, display a number."""
        if not n:
            btn["text"] = "Done."
            return
        else:
            temp = n.pop()
            # make the button show the number
            btn["text"] = str(temp)
            # display the number on the label.
            lbl[temp-1]["text"] = str(temp)

def main():
    # set up variables
    top_number = 90 # please use a multiple of ten
    numbers = list(range(1, top_number + 1))
    shuffle(numbers)
    my_labels, k, underscores = [], 0, "___"
    
    # set up GUI
    root = Tk()
    bingo = Frame(root)
    bingo.grid()
    root.title("Bingo")

    # create the labels 
    for i in range(top_number //10):
        for j in range(10):
            my_labels.append(Label(bingo, text = underscores))
            my_labels[k].grid(row = i, column = j)
            k +=1
            
    #create a button
    my_button = Button(bingo, text = "Click.")
    my_button["command"] = lambda: get_number(numbers, my_labels, my_button)
    my_button.grid(column = 3, columnspan = 4, pady = 5)

    # bind return key to avoid the need to click
    root.bind('<Return>', lambda: get_number(numbers, my_labels, my_button))

    root.mainloop()

# call main function
if __name__ == "__main__":
        main()
