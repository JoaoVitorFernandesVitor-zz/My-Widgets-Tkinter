from tkinter import *
from Widgets import Entry_Validater as entry

screen = Tk()
screen.geometry('600x500+250+250')

Entry()
a = Frame(screen)
a.place(x = 50, y = 20)
b = entry.entry_Valition(a,'Helo world', show_fg= '#b1e0db',caracter= False)

# botão
x = Button(a, text = 'Validader', command =b.Validar)
x.grid()


screen.mainloop()