from tkinter import * 

#Entrada de texto com validação para senhas
class entry_Valition(Entry):
        
    def __init__(self, parent,
    show_text = '',# texto q vai aparecer enquanto nao se digita nd
    show_font = '',
    show_fg = '',
    font = '',
    fontcollor = '',
    font_default = 'Arial 8', fg_default = '#000000',
    fail = '',
    name = '' #Nome para formatação Ex: User ou Password
):  
        super().__init__()
        #Propriedades da entry
        self.name = name
        self.fail = fail
        self.font = font
        self.fontcollor = fontcollor
        self.show_text = show_text
        self.show_fg = show_fg

        if show_font != '':
            self['font']= show_font

        if show_fg != '':
            self['fg']= show_fg


        self.insert(0, show_text)#Cria o texto na entry
        #Show delet
        def del_show():
            self.delete(0, END)
            #Altera a fonte para a padrao  ou o indicada
            if font != '':
                self['font'] = font

            else:
                self['font'] = font_default

            if fontcollor != '':
                self['fg']= fontcollor
            
            else:
                self['fg'] = fg_default


        self['validate'] = 'focusin'
        self['vcmd'] = del_show
        
        #Grid
        self.grid(in_ = parent)
        

    def Validar(self, min = 8, max = 100):
        texto = self.get()
        #Reporta se estiver em branco
        if texto == '':
            self.fail = f'{self.name} em braco não é valido!'
            
        else:            
            #Reporta se estiver abaixo do min de digitos
            if len(texto) < min :
                self.fail = f'{self.name} deve conter no min {min} digitos!'
            
            else:
                #Reporta se estiver acima do max de digitos
                if len(texto) > max:
                    self.fail = f'{self.name} deve conter no max {max} digitos!'
                    
                else:
                    #Reporta se nao conter caracteres especiais
                    if texto.isupper :
                        self.fail = f'{self.name} deve conter letras maiúsculas e minúsculas, números e caracteres especiais!'
                    
                    else:
                        self.fail = f'{self.name} é valido'
                
        print(self.fail)
                