import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("MINESWEEPER")

#
sel_frame = tk.Frame(root)
sel_frame.grid(row=0,column=0)

var = tk.IntVar()

e_frame = tk.Frame(root)
e_frame.grid(row=0,column=0)

m_frame = tk.Frame(root)
m_frame.grid(row=0,column=0)

h_frame = tk.Frame(root)
h_frame.grid(row=0,column=0)

class Selection:  
    def __init__(self,display):
        self.display = display
        
        self.title = tk.Label(display,text="SELECT MODE")
        self.title.grid(row=0,column=1)

        self.easy_sel = tk.Radiobutton(display,text="EASY",variable=var,value=0)
        self.easy_sel.grid(row=1,column=0)

        self.med_sel = tk.Radiobutton(display,text="MEDIUM",variable=var,value=1)
        self.med_sel.grid(row=1,column=1)

        self.hard_sel = tk.Radiobutton(display,text="HARD",variable=var,value=2)
        self.hard_sel.grid(row=1,column=2)        
    
        self.submit_b = tk.Button(display,text="SUBMIT",command=submit)
        self.submit_b.grid(row=2,column=1)

class Button:
    def __init__(self,display,row,column,command):
        self.display = display

        self.row = row
        
        self.column = column

        self.command = command
    
    def make(self):
        b = tk.Button(self.display,width=3)
        b.grid(row=self.row,column=self.column)

class Back_Button:
    def __init__(self,display,x,y,command):
        self.display = display

        self.x = x

        self.y = y

        self.command = command
    
    def make(self):
        b_button = tk.Button(self.display,text="BACK",command=self.command)
        b_button.place(x=self.x,y=self.y)

class Easy_Board:
    def __init__(self,display):
        self.display = display      

        for i in range(6):
            for a in range(6):
                b = Button(self.display,i,a,blank)
                b.make()

        back_b = Back_Button(display,100,100,blank)
        back_b.make()

class Medium_Board:
    def __init__(self,display):
        self.display = display      

        for i in range(9):
            for a in range(9):
                b = Button(self.display,i,a,blank)
                b.make()
        
        back_b = Back_Button(display,100,100,blank)
        back_b.make()

class Hard_Board:
    def __init__(self,display):
        self.display = display      

        for i in range(15):
            for a in range(15):
                b = Button(self.display,i,a,blank)
                b.make()

        back_b = Back_Button(display,100,100,blank)
        back_b.make()

def blank():
    print("test")

def submit():
    if var.get() == 0:
        e = Easy_Board(e_frame)
        e_frame.tkraise
        sel_frame.grid_forget()

    elif var.get() == 1:
        m = Medium_Board(m_frame)
        m_frame.tkraise
        sel_frame.grid_forget()

    elif var.get() == 2:
        h = Hard_Board(h_frame)
        h_frame.tkraise
        sel_frame.grid_forget()

def back():
    s = Selection(sel_frame)
    sel_frame.tkraise()
    e_frame.grid_forget()
    m_frame.grid_forget()
    h_frame.grid_forget()

sel_frame.tkraise()
s = Selection(sel_frame)

#loop
root.mainloop()