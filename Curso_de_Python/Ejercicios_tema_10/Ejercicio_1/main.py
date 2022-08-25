'''En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
y que contenga un botón de reinicio para que deje todos como al principio.
Al principio no tiene que haber una opción seleccionada.'''

import tkinter
from tkinter import ttk

class Window():
    # creamos la ventana
    window = tkinter.Tk()
    selection = tkinter.StringVar()

    def __init__(self):
        # creamos un grid en la ventana
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=3)

        # mostramos componentes
        self.printComponents(self.window)
        
    def printComponents(self, window):     
        # creamos los radiobuttons        
        radio1 = ttk.Radiobutton(self.window, text="opción 1", value='1', variable=self.selection)
        radio2 = ttk.Radiobutton(self.window, text="opción 2", value='2', variable=self.selection)
        radio3 = ttk.Radiobutton(self.window, text="opción 3", value='3', variable=self.selection)
        radio4 = ttk.Radiobutton(self.window, text="opción 4", value='4', variable=self.selection)

        # posicionamos los radiobuttons
        radio1.grid(column=0, row=1, pady=5, padx=5)
        radio2.grid(column=0, row=2, pady=5, padx=5)
        radio3.grid(column=0, row=3, pady=5, padx=5)
        radio4.grid(column=0, row=4, pady=5, padx=5)

        # creamos un boton para limpiar la selección
        boton_limpiar= tkinter.Button(window, text="Reiniciar")
        boton_limpiar.bind('<Button-1>', self.clearSelection)

        # posicionamos el boton
        boton_limpiar.grid(column=3, row=5, pady=5, padx=5)

    
    def clearSelection(self, event):
        #deseleccionamos los radiobuttons
        self.selection.set(" ")

def main():
    ventana = Window()
    Window.window.mainloop()


if __name__ == "__main__":
    main()