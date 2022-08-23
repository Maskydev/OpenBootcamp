''' Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.'''


def main():
    def formatear(x):
        if x.startswith(' '):
            x = x.strip()

        x = x.capitalize()
        return x

    paises = []

    entrada = input("Escribe una lista de paises separados por ',' :")

    paises = entrada.split(", ")
    paisesFormateado = map(formatear, paises)
    print(list(sorted(paisesFormateado)))


if __name__ == "__main__":
    main()
