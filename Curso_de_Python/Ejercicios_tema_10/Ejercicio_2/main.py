''' En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener 
una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.'''

import tkinter
from tkinter import ttk

class Window():
    # creamos la ventana
    window = tkinter.Tk()    

    def __init__(self):
        # creamos un grid en la ventana
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=3)

        # mostramos componentes
        self.printComponents(self.window)
        
    def printComponents(self, window):  

        ## labels pack pack ruedas
        packs = ttk.Label(self.window, text="Packs y Accesorios:")     
        packsRuedas = ttk.Label(self.window, text="Packs ruedas:")         
        
        #check buttons
        selection1 = tkinter.StringVar() 
        selection2 = tkinter.StringVar() 
        selection3 = tkinter.StringVar() 
        llanta = ttk.Checkbutton(self.window, text="Llantas de aleación", variable=selection1)
        tuerca = ttk.Checkbutton(self.window, text="Tuercas de seguridad", variable=selection2)
        kit = ttk.Checkbutton(self.window, text="Kit eléctrico para inflar neumáticos ", variable=selection3)
        # posicionamos el contenido
        packs.grid(column=0, row=1, pady=5, padx=5)
        packsRuedas.grid(column=0, row=2, pady=5, padx=5)
        llanta.grid(column=1, row=3, pady=5, padx=5)
        tuerca.grid(column=2, row=3, pady=5, padx=5)
        kit.grid(column=3, row=3, pady=5, padx=5)
        
        ## labels pack Estilo exterior
        estilo = ttk.Label(self.window, text="Estilo exterior:")         
        selection4 = tkinter.StringVar() 
        selection5 = tkinter.StringVar() 
        selection6 = tkinter.StringVar() 
        guardabarro = ttk.Checkbutton(self.window, text="Embellecedor guardabarros ", variable=selection4)
        frontal = ttk.Checkbutton(self.window, text="Embellecedor frontal ", variable=selection5)
        maletero = ttk.Checkbutton(self.window, text="Embellecedor maletero", variable=selection6)
        # posicionamos el contenido
        estilo.grid(column=0, row=4, pady=5, padx=5)
        guardabarro.grid(column=1, row=5, pady=5, padx=5)
        frontal.grid(column=2, row=5, pady=5, padx=5)
        maletero.grid(column=3, row=5, pady=5, padx=5)



def main():
    ventana = Window()
    Window.window.mainloop()

if __name__ == "__main__":
    main()