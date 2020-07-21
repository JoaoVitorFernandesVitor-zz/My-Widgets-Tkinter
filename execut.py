from tkinter import *
from Widgets import Chat as c

screen = Tk()
screen.geometry('600x500+250+250')
c.Chat(screen)

screen.mainloop()