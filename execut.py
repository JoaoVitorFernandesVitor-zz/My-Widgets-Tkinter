from tkinter import *
from Widgets import Formulario as f

screen = Tk()
screen.geometry('600x500+250+250')

a = f.Formulario().grid()

screen.mainloop()