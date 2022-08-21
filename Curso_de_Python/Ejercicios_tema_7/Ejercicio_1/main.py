''' En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.''' 

import operaciones


def main():
    suma = operaciones.sumar(4,4)
    resta = operaciones.restar (15, 5)
    multiplicacion = operaciones.multiplicar(6, 6)
    division = operaciones.dividir (40, 2)

    print("suma:", suma)
    print("resta:", resta)
    print("multiplicación:", multiplicacion)
    print("división:", division)

if __name__ == '__main__' :
    main()