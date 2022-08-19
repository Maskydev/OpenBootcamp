# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero_inicial = int(input("¿Número inicial? "))
numero_final = int(input("¿Número Final? "))
listaImpares = []

for numero in range(numero_inicial, numero_final):
    if(numero % 2 != 0):
        listaImpares.append(numero)

print(listaImpares)