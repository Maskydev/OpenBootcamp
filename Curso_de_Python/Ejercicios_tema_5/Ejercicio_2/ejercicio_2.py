# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def esPrimo(numero):
    primo = 0
    for valor in lista:
        if (numero % valor == 0):
            primo += 1

    if (primo >= 1) :
        primo = False
    else:
        primo = True
    return primo          

numero = int(input("Escribe un número: "))
lista = list(range(2, numero))

if esPrimo(numero):
    print(numero, "es un numero primo.")
else:
    print(numero, "no es un numero primo.")
