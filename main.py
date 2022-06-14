import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("MINESWEEPER")

class Selection:
    def __init__(self,display):
        self.display = display
        
        self.title = tk.Label(display,text="SELECT MODE")
        self.title.grid(row=0,column=1)

        self.var = tk.IntVar()

        self.easy_sel = tk.Radiobutton(display,text="EASY",variable=self.var,value=0)
        self.easy_sel.grid(row=1,column=0)

        self.med_sel = tk.Radiobutton(display,text="MEDIUM",variable=self.var,value=1)
        self.med_sel.grid(row=1,column=1)

        self.hard_sel = tk.Radiobutton(display,text="HARD",variable=self.var,value=2)
        self.hard_sel.grid(row=1,column=2)        
    
        self.submit_b = tk.Button(display,text="SUBMIT")
        self.submit_b.grid(row=2,column=1)

    def submit(self):
        if self.var == 0:
            return "e"
        elif self.var == 1:
            return "m"
        else:
            return "h"

s = Selection(root)
s.submit()

#functions
# def submit():
#     if var.get() == 0:
#         easy_board()
#     elif var.get() == 1:
#         medium_board()
#     else:
#         hard_board()

# def back():
#     selection_frame.tkraise()
#     easy_frame.grid_forget()
#     med_frame.grid_forget()
#     hard_frame.grid_forget()

# class Back_Button:
#     def __init__(self,display,row,column,text,command):
#         self.display = display
#         self.row = row
#         self.column = column
#         self.text = text
#         self.command = command
#     def make(self):
#         b = tk.Button(self.display,text=self.text,command=self.command)
#         b.grid(row=self.row,column=self.column)

# #selection frame
# def selection():
#     global selection_frame
#     selection_frame = tk.Frame(root)
#     selection_frame.grid(row=0,column=0)

#     selection_title = tk.Label(selection_frame,text="SELECT MODE")
#     selection_title.grid(row=0,column=1)

#     var = tk.IntVar()

#     easy_sel = tk.Radiobutton(selection_frame,text="EASY",variable=var,value=0)
#     easy_sel.grid(row=1,column=0)

#     med_sel = tk.Radiobutton(selection_frame,text="MEDIUM",variable=var,value=1)
#     med_sel.grid(row=1,column=1)

#     hard_sel = tk.Radiobutton(selection_frame,text="HARD",variable=var,value=2)
#     hard_sel.grid(row=1,column=2)

#     submit = tk.Button(selection_frame,text="SUBMIT",command=submit)
#     submit.grid(row=2,column=1)

# #boards

# def easy_board():
#     easy_frame = tk.Frame(root)
#     easy_frame.grid(row=0,column=0)

#     back_b = Back_Button(easy_frame,0,0,"BACK",back)
#     back_b.make()

# def medium_board():
#     med_frame = tk.Frame(root)
#     med_frame.grid(row=0,column=0)

#     back_b = Back_Button(med_frame,0,0,"BACK",back)
#     back_b.make()

# def hard_board():
#     hard_frame = tk.Frame(root)
#     hard_frame.grid(row=0,column=0)

#     back_b = Back_Button(hard_frame,0,0,"BACK",back)
#     back_b.make()

# selection()
# selection_frame.tkraise()

root.mainloop()
