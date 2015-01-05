# caesar_cipher.py: simple message coder / decoder 

# get the GUI building module
from tkinter import *

# make two strings that hold upper and lower case alphabets.
u_case  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo_case = "abcdefghijklmnopqrstuvwxyz"

# function definition for the buttons
def submit(action):
    # get the text from the entry boxes
    plain_text = in_ent.get()
    key = key_ent.get()
    # check there is a message
    if plain_text == "":
        display("You haven't entered a message.")
        return
    # check that the key is a number
    try:
        key = int(key)
    except ValueError:
        display("Please enter a numerical key.")
        return
    # check the key is between -26 and 26
    if key < -26 or key > 26: 
       display("Please use a key between -26 and 26.")
       return
    
    # Encode / decode
    cipher_text = ""
    # Check if we are decoding
    if action == "decode":
        key = -key 
    # loop over the letters and make the new string
    for letter in plain_text:
        if letter in u_case:
            temp = u_case
        elif letter in lo_case:
            temp = lo_case
        # Don't change characters that are not in the alphabet
        else:
            cipher_text = cipher_text + letter
            continue
        # put the index of the letter in i
        i = temp.find(letter)
        # make j the index plus the key
        j = i + key
        # the modulus will take care of numbers < 0 or > 26
        cipher_text = cipher_text + temp[j % 26]         
    
    # clear text entry box and print message
    in_ent.delete(0, END)
    display(cipher_text)

def display(message):
    # clear the display box and print the message
    txt.delete(0.0, END)
    txt.insert(0.0, message)

# make the GUI
# create the "root" window 
root = Tk()
root.title("Secret Code")
root.geometry("600x350")
app = Frame(root)
app.grid()

# setting up the GUI
lbl = Label(app, text = "Welcome to Secret Code!")
lbl.grid(row = 0, column = 1,  pady = 5, sticky = W)

in_lbl = Label(app, text = "Secret Message:")
in_lbl.grid(row = 1, column = 0, pady = 5)
in_ent = Entry(app, width = 30)
in_ent.grid(row = 1, column = 1, pady = 5)

key_lbl = Label(app, text = "Input a key\n (-26 to 26):")
key_lbl.grid(row = 2, column = 0, pady = 5)
key_ent = Entry(app, width = 2)
key_ent.grid(row = 2, column = 1, pady = 5, sticky = W)

bttn = Button(app, text = "Encode!")
bttn["command"] = lambda: submit("encode")
bttn.grid(row = 3, column = 0, pady = 5)  

bttn = Button(app, text = "Decode!")
bttn["command"] = lambda: submit("decode")
bttn.grid(row = 3, column = 1, pady = 5)  

msg_lbl = Label(app, text = "Code:")
msg_lbl.grid(row = 5, column = 0, pady = 5)
txt = Text(app, width = 50, height = 10, wrap = WORD)
txt.grid(row = 5, column = 1, pady = 5)

# Start the main-loop (like in a game).
root.mainloop()
