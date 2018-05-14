#!/usr/bin/python

import tkinter
from tkinter import ttk #ttk gir en mer "fancy" look enn tk som har et mer basic preg
top = tkinter.Tk()

# kode til widgets
class programmet():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Super Nice GUI")
        self.create_widgets()

    def create_widgets(self):
        #lage litt padding rundt hver ting
        self.window['padx'] = 10
        self.window['pady'] = 10

w =  ttk.Button (top, text= "knapp")
w.pack()



top.mainloop()
