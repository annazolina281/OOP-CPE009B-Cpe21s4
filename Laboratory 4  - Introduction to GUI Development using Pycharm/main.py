from registration import MyWindow
from tkinter import *

window = Tk()
MyWin=MyWindow(window)
window.geometry("400x350+10+10")
window.title("Standard Calculator")
window.mainloop()