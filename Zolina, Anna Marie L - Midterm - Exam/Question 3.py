from tkinter import *
from tkinter import messagebox

class MyWindow:
    def __init__(self, win):

        self.Label1 = Label(win, fg="BLACK", text="Hello!", font=("Times New Roman", 15))
        self.Label1.place(x=20, y=25)

        self.Label2 = Label(win, fg="Red", text = "Enter your fullname: ", font = ("Times New Roman",12,))
        self.Label2.place(x=20, y=60)

        self.Entry1 = Entry(win, bd=5)
        self.Entry1.place(x=200, y=60)

        self.Button2 = Button(win, fg="Red", height=1, width=23, text="Click to display your fullname", font = ("Times New Roman",9,), command=self.show)
        self.Button2.place(x=17, y=100)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=200, y=100)

    def show(self):
        result = self.Entry1.get()
        self.Entry2.insert(END, str(result))

window = Tk()
MyWin=MyWindow(window)
window.geometry("400x350+10+10")
window.title("Midterm in OOP")
window.mainloop()
