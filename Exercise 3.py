from tkinter import*

class MyWindow:
    def __init__(self, win):
        #commonwidgets

        win.config(bg = "PINK")
        self.Label1 = Label(win, fg="GRAY", text = "CALCULATOR :)))", font = ("Times New Roman",15))
        self.Label1.place(x=110, y=25)

        self.Label2 = Label(win, fg="GRAY", text = "NUMBER 1: ", font = ("Times New Roman",8))
        self.Label2.place(x=90, y=80)

        self.Entry1 = Entry(win, bd=5)
        self.Entry1.place(x=175, y=80)

        self.Label3 = Label(win, fg="GRAY", text="NUMBER 2: ", font = ("Times New Roman",8))
        self.Label3.place(x=90, y=130)

        self.Entry2 = Entry(win, bd=5)
        self.Entry2.place(x=175, y=130)

        self.Label4 = Label(win, fg="GRAY", text="RESULT: ", font = ("Times New Roman",8))
        self.Label4.place(x=90, y=180)

        self.Entry3 = Entry(win, bd=5)
        self.Entry3.place(x=175, y=180)

        self.Button1 = Button(win, fg="GRAY", text = "Add", command= self.add)
        self.Button1.place(x=70, y =230)

        self.Button2 = Button(win, fg="GRAY", text="Subtract", command=self.sub)
        self.Button2.place(x=110, y=230)

        self.Button3 = Button(win, fg="GRAY", text="Multiply", command=self.mul)
        self.Button3.place(x=171, y=230)

        self.Button4 = Button(win, fg="GRAY", text="Division", command=self.div)
        self.Button4.place(x=232, y=230)

        self.Button5 = Button(win, fg="GRAY", text="Clear", command=self.clear)
        self.Button5.place(x=291, y=230)
        self.Button5.bind('<Button-1>', self.clear)

    def add(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, 'end')
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))

    def clear(self):
        self.Entry1.delete(0, 'end')
        self.Entry2.delete(0, 'end')
        self.Entry3.delete(0, 'end')


window = Tk()
MyWin=MyWindow(window)
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()
