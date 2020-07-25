from tkinter import *
from Widgets import Chat as f

screen = Tk()
screen.geometry('600x500+250+250')

f.Chat('Yuki').grid()

screen.mainloop()