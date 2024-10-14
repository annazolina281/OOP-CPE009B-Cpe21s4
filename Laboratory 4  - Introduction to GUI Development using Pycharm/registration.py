from tkinter import *
from tkinter import messagebox

class MyWindow:
    def __init__(self, win):

        self.Label1 = Label(win, fg="BLACK", text = "Account Registration System", font = ("Times New Roman",15))
        self.Label1.place(x=85, y=25)

        self.Label2 = Label(win, fg="BLACK", text = "First Name: ", font = ("Arial",8,))
        self.Label2.place(x=90, y=60)

        self.Entry1 = Entry(win, bd=5)
        self.Entry1.place(x=175, y=60)

        self.Label3 = Label(win, fg="BLACK", text="Last Name: ", font = ("Arial",8))
        self.Label3.place(x=90, y=100)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=175, y=100)

        self.Label4 = Label(win, fg="BLACK", text="Username: ", font = ("Arial",8))
        self.Label4.place(x=90, y=140)

        self.Entry3 = Entry(win, bd=5)
        self.Entry3.place(x=175, y=140)

        self.Label5 = Label(win, fg="BLACK", text="Password: ", font=("Arial", 8))
        self.Label5.place(x=90, y=180)

        self.Entry4 = Entry(win, bd=5, show = '*')
        self.Entry4.place(x=175, y=180)

        self.Label6 = Label(win, fg="BLACK", text="Email Address: ", font=("Arial", 8))
        self.Label6.place(x=90, y=220)

        self.Entry5 = Entry(win, bd=5)
        self.Entry5.place(x=175, y=220)

        self.Label7 = Label(win, fg="BLACK", text="Contact Number: ", font=("Arial", 8))
        self.Label7.place(x=90, y=260)

        self.Entry6 = Entry(win, bd=5)
        self.Entry6.place(x=175, y=260)

        self.Button = Button(win, fg="BLACK",height =1, width = 15, text="Clear", command=self.clear)
        self.Button.place(x=210, y=300)

        self.Button2 = Button(win, fg="BLACK", height=1, width=15, text="Submit", command=self.submit)
        self.Button2.place(x=80, y=300)


    def submit(self):
        messagebox.showinfo('Account Registration', 'Your Account Has Been Verified!')
    def clear(self):
        self.Entry1.delete(0, 'end')
        self.Entry2.delete(0, 'end')
        self.Entry3.delete(0, 'end')
        self.Entry4.delete(0, 'end')
        self.Entry5.delete(0, 'end')
        self.Entry6.delete(0, 'end')

