from tkinter import *
from Widgets import *

screen = Tk()
screen.geometry('600x500+250+250')


a = Frame(screen)
a.place(x = 50, y = 20)
b = entry_Valition(a,'Helo world', show_fg= '#b1e0db')

# botão
x = Button(a, text = 'Validader', command =b.Validar)
x.grid()


screen.mainloop()