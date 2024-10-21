from tkinter import *
from tkinter import messagebox
import os

class MyWindow:
    def __init__(self, win):
        self.filename = "registration.txt"

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

    def clear(self):
            self.Entry1.delete(0, 'end')
            self.Entry2.delete(0, 'end')
            self.Entry3.delete(0, 'end')
            self.Entry4.delete(0, 'end')
            self.Entry5.delete(0, 'end')
            self.Entry6.delete(0, 'end')

    def submit(self):
        entries = {
            "First Name": self.Entry1.get(),
            "Last Name": self.Entry2.get(),
            "Username": self.Entry3.get(),
            "Password": self.Entry4.get(),
            "Email": self.Entry5.get(),
            "Contact Number": self.Entry6.get()
        }

        # Check if any entry is empty
        for blank, value in entries.items():
            if not value:
                messagebox.showwarning("Input Error", f"{blank} is required!")
                return
        messagebox.showinfo('Registration Success', 'Your account has been successfully registered!')

        # Save to text file
        with open(self.filename, 'a') as file:
            file.write(f"First Name: {self.Entry1.get()}, Last Name: {self.Entry2.get()}, "
                       f"Username: {self.Entry3.get()}, Password: {self.Entry4.get()}, "
                       f"Email: {self.Entry5.get()}, Contact Number: {self.Entry6.get()}\n")



