from tkinter import *

tela = Tk()
class Formulario(Frame):
        def __init__(self, parent):
        #Propriedades do Formulario

            #Variables from RadioButtons
            gender = StringVar()
            formation = StringVar()
            title_font =  'Arial 20'
            #Dados Privados
            name_entry = Entry(self)
            name_text  = Label(self, text = 'Your Name', font = title_font)

            years_entry = Entry(self)
            years_text  = Label(self, text = 'Years old', font = title_font)

            gender_male   = Radiobutton(self, text = 'Male', variable = gender, value = 'male')
            gender_female = Radiobutton(self, text = 'Female', variable = gender, value = 'female')
            gender_text   = Label(self, text = 'Gender', font = title_font)


            profession_entry = Entry(self)
            profession_text  = Label(self, text = 'Profession', font = title_font)

            nationality_entry = Entry(self)
            nationality_text  = Label(self, text = 'Nationality', font = title_font)

            formation_technician = Radiobutton(self, variable = formation, text = 'Technician', value = 'technician')
            formation_higher = Radiobutton(self, variable = formation, text = 'Higher - University', value = 'higher')
            formation_high = Radiobutton(self, variable = formation, text = 'High School', value = 'high school')
            formation_text = Label(self, text = 'Formation', font = title_font)

            email_entry = Entry(self)
            email_text = Label(self, text = 'Email', font = title_font)

            #Grids Dados Privados
            name_text.grid(row = 0 , column = 0, sticky = W)
            name_entry.grid(row = 0 , columnspan = 2, column = 1)

            years_text.grid(row = 1, column = 0, stick = W)
            years_entry.grid(row = 1, columnspan = 2, column = 1)

            gender_text.grid(row = 2, column = 0, stick = W)
            gender_male.grid(row = 3, column = 0, stick = W)
            gender_female.grid(row = 4, column = 0, stick = W)

            profession_text.grid(row = 5, column = 0, stick = W)
            profession_entry.grid(row = 5, columnspan = 2, column = 1)

            nationality_text.grid(row = 6, column = 0, stick = W)
            nationality_entry.grid(row = 6 , columnspan = 2, column = 1)
            
            formation_text.grid(row = 7, column = 0, stick = W)
            formation_high.grid(row = 8, column = 0, stick = W)
            formation_higher.grid(row = 9, column = 0, stick = W)
            formation_technician.grid(row = 10, column =0, stick = W)

            email_text.grid(row = 11, column = 0, stick = W)
            email_entry.grid(row = 11, columnspan = 2, column = 1, stick = W)
            
            self.grid(parent)
tela.mainloop()