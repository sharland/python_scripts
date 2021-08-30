# v=u + at
from tkinter import *
# create the radio button widget
class Application(Frame):
    def __init__(self, master):
        # initialise frame
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create widgets for choices via radio buttons
        # create description label
        Label(self,
              text = "Select the correct version of the formula you require"
              ).grid(row = 0, column = 0, sticky = W)
        # create instruction label
        Label(self,
              text = "Select one:"
              ).grid(row=1,column = 0,sticky = W)
        #create variable for single formula
        self.favorite = StringVar()
        self.favorite.set(None) # empty string
        #create v=u+at button
        Radiobutton(self,
                    text = "v = u + at",
                    variable = self.favorite,
                    value = "v=u+at",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

   
        #create v2=u2-2as button
        Radiobutton(self,
                    text = "v2 = u2 - 2as",
                    variable = self.favorite,
                    value = "v2=u2-2as",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

    
        #create s=ut-0.5at2 button
        Radiobutton(self,
                    text = "s=ut-0.5at2",
                    variable = self.favorite,
                    value = "s=ut-0.5at2",
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        # create submit button
        self.submit_bttn = Button(self, text = "Submit")
        #self.submit_bttn.grid(row = 7, column = 0, sticky = W)
        self.submit_bttn["command"] = self.assign_u

    
    def assign_u(self):
    
        contents = self.u_ent.get()
        u = float(contents)

        contents = self.a_ent.get()
        a = float(contents)

        contents = self.t_ent.get()
        t = float(contents)

        v = u + a*t
        self.answer_lbl = Label(self, text = "V = " + str(v))
        self.answer_lbl.grid(row = 9, column = 0, columnspan = 2, sticky = W)

        print(v)
        
      
    def update_text(self):
        #update text area and display formula chosen
       
        # remove any previous text before inserting the text created above
        message = ""
        
        
        formula =""
        formula += self.favorite.get()
        if formula == "v=u+at" :
            message = "Your chosen formula is correct"
        if formula != "v=u+at" :
            #update text area and display formula chosen
            message = "Your chosen formula is incorrect" 
        
        #create text box to display result
        self.results_txt = Text(self,width= 40, height = 1,wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message) 

        if formula == "v=u+at" :
           
            #Create text, and entry widgets.
            #create instruction label
            
            self.inst_lbl = Label(self, text = "Enter a value for u")
            self.inst_lbl.grid(row = 6, column = 0, columnspan = 2, sticky = W)
            self.inst_lbl = Label(self, text = "Enter a value for a")
            self.inst_lbl.grid(row = 7, column = 0, columnspan = 2, sticky = W)
            self.inst_lbl = Label(self, text = "Enter a value for t")
            self.inst_lbl.grid(row = 8, column = 0, columnspan = 2, sticky = W)
            
                   
            # create entry widget to accept u      
            self.u_ent = Entry(self)
            self.u_ent.grid(row = 6, column = 1, sticky = W)

             # create entry widget to accept a      
            self.a_ent = Entry(self)
            self.a_ent.grid(row = 7, column = 1, sticky = W)

             # create entry widget to accept t      
            self.t_ent = Entry(self)
            self.t_ent.grid(row = 8, column = 1, sticky = W)
           
            # display submit button
            
            self.submit_bttn.grid(row = 9, column = 3)
            

                
#create the root window
root = Tk()
#modify the window
root.title("v = u + at")
#create the main screen
app = Application(root)
app.grid()


#kick off the window's event loop
root.mainloop()



