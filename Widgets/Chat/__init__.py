from tkinter import *
 
class Chat(Frame):
    def __init__(self,parent):
        super().__init__()
        def Send():
            text_chat['state'] = NORMAL
            text_send = entry_chat.get()
            text_chat.insert(END,text_send)
            text_chat['state']= DISABLED

        #Widgets internos
        text_chat = Text(self,bg = 'blue' , width = 30, state = DISABLED) 
        entry_chat = Entry(self)
        send_button = Button(self, text = 'Send', command = Send)
    
        #Widgets Grids
        text_chat.grid()
        entry_chat.grid(row = 1)
        send_button.grid(row = 1, column = 1)
        self.grid()