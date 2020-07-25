from tkinter import *

tela = Tk()
def init(parent):
    #Propriedades do Formulario
    
    #Variables from RadioButtons
    gender = StringVar()
    formation = StringVar()
    title_font =  'Arial 20'
    #Dados Privados
    name_entry = Entry(parent)
    name_text  = Label(parent, text = 'Your Name', font = title_font)

    years_entry = Entry(parent)
    years_text  = Label(parent, text = 'Years old', font = title_font)

    gender_male   = Radiobutton(parent, text = 'Male', variable = gender, value = 'male')
    gender_female = Radiobutton(parent, text = 'Female', variable = gender, value = 'female')
    gender_text   = Label(parent, text = 'Gender', font = title_font)


    profession_entry = Entry(parent)
    profession_text  = Label(parent, text = 'Profession', font = title_font)

    nationality_entry = Entry(parent)
    nationality_text  = Label(parent, text = 'Nationality', font = title_font)

    formation_technician = Radiobutton(parent, variable = formation, text = 'Technician', value = 'technician')
    formation_higher = Radiobutton(parent, variable = formation, text = 'Higher - University', value = 'higher')
    formation_high = Radiobutton(parent, variable = formation, text = 'High School', value = 'high school')
    formation_text = Label(parent, text = 'Formation', font = title_font)

    #Grids Dados Privados
    name_text.grid(row = 0 , columnspan = 2, column = 0, sticky = W)
    name_entry.grid(row = 0 , column = 2)

    years_text.grid(row = 1, columnspan = 2, column = 0, stick = W)
    years_entry.grid(row = 1, column = 2)

    gender_text.grid(row = 2, columnspan = 2, column = 0, stick = W)
    gender_male.grid(row = 3, column = 1, stick = W)
    gender_female.grid(row = 4, column = 1, stick = W)

    profession_text.grid(row = 5, columnspan = 2, column = 0, stick = W)
    profession_entry.grid(row = 5, column = 2)
    
    formation_text.grid(row = 6, columnspan = 2, column = 0, stick = W)
    formation_high.grid(row = 7, column = 1, stick = W)
    formation_higher.grid(row = 8, column = 1, stick = W)
    formation_technician.grid(row = 9, column = 1, stick = W)

    #Dados de segurança
    senha_entry = Entry(parent)
    senha_text  = Label(parent, text = 'Password' , font = title_font)
    
    

init(tela)


tela.mainloop()