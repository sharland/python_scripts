# v=u + at
from tkinter import *
#import graph
import csv
global A0,v,u,a,t,correct,correct_count, percentage,answer

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
        self.update_bttn = Button(self, text = "update")
        #self.submit_bttn.grid(row = 7, column = 0, sticky = W)
        self.update_bttn["command"] = self.update_text
        # create submit button
        self.submit_bttn = Button(self, text = "Submit")
        #self.submit_bttn.grid(row = 7, column = 0, sticky = W)
        self.submit_bttn["command"] = self.assign_u
        

    
    def assign_u(self):
        
        global A0,v,u,a,t,answer

        A0 = self.A0_ent.get()
      
    
        contents = self.u_ent.get()
        u = float(contents)

        contents = self.a_ent.get()
        a = float(contents)

        contents = self.t_ent.get()
        t = float(contents)

        contents = self.answer_ent.get()
        answer = round(float(contents),2)

        v = u + a*t
        v = round(v,2)
        self.answer_lbl = Label(self, text ="V = " + str(v))
        self.answer_lbl.grid(row = 10, column = 0, columnspan = 2, sticky = W)

        create_file()
        read_file()
        search_file()
        
        #graph.draw_line() # calls draw line module
        
      
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
            self.inst_lbl = Label(self, text = "Enter A0....")
            self.inst_lbl.grid(row = 5, column = 0, columnspan = 2, sticky = W)
            self.inst_lbl = Label(self, text = "Enter a value for u")
            self.inst_lbl.grid(row = 6, column = 0, columnspan = 2, sticky = W)
            self.inst_lbl = Label(self, text = "Enter a value for a")
            self.inst_lbl.grid(row = 7, column = 0, columnspan = 2, sticky = W)
            self.inst_lbl = Label(self, text = "Enter a value for t")
            self.inst_lbl.grid(row = 8, column = 0, columnspan = 2, sticky = W)
            self.inst_lbl = Label(self, text = "Enter your answer")
            self.inst_lbl.grid(row = 9, column = 0, columnspan = 2, sticky = W)
            
             # create entry widget to accept A0....      
            self.A0_ent = Entry(self)
            self.A0_ent.grid(row = 5, column = 1, sticky = W)
            
            # create entry widget to accept u      
            self.u_ent = Entry(self)
            self.u_ent.grid(row = 6, column = 1, sticky = W)

             # create entry widget to accept a      
            self.a_ent = Entry(self)
            self.a_ent.grid(row = 7, column = 1, sticky = W)

             # create entry widget to accept t      
            self.t_ent = Entry(self)
            self.t_ent.grid(row = 8, column = 1, sticky = W)
            
            # create entry widget to accept your answer      
            self.answer_ent = Entry(self)
            self.answer_ent.grid(row = 9, column = 1, sticky = W)
           
            # display submit button
            
            self.submit_bttn.grid(row = 9, column = 3)
            
            # save values to file
            
def create_file():
    print('writing')
    currentFile = open("results.csv","a") #append to existing file
    correct = 0
    if answer == v:
        correct = 1
    newline =  A0 + "," + str(correct)+ "," + str(v) + "," + str(u) + "," + str(a) + "," +str(t)
    newline += ("\n")#puts each string on a new line in csv file
    currentFile.write(newline)
    currentFile.close()
    return



def read_file():
    print('reading')
    reader = csv.reader(open("results.csv"))
    for A0,correct,v,u,a,t in reader:
        print(A0," ",correct , " ",v," ",u," ",a," ",t)
        print("\n")
    return
           
def search_file():
    
    count = 0
    correct_count=0
    no_of_records = 0
   # print('reading')
    reader = csv.reader(open("results.csv"))
    for A0,correct,v,u,a,t in reader:
        if A0 == "1234":
            print(A0," ",correct," ",v," ",u," ",a," ",t)
            print("\n")
            count += 1
           # print('count=', count)
            if int(correct) == 1:
              correct_count += 1
        no_of_records += 1
       
   # print(correct_count)
    percentage = correct_count/count
    percentage = round(percentage*100,2)
    print("Percentage correct ", percentage,"%")
              
            
    return        

                
#create the root window
root = Tk()
#modify the window
root.title("v = u + at")
#create the main screen
app = Application(root)
app.grid()


#kick off the window's event loop
root.mainloop()



