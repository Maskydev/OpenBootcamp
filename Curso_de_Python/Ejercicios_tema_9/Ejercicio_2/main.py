''' En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos 
impares de una lista pasada por parámetro con filter y realizará una suma de todos estos 
elementos obtenidos mediante reduce.'''
from  functools import reduce


def main():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    listaImpares = filter(lambda x: x % 2, lista)
    suma = reduce(lambda a,b: a+b ,listaImpares)
    print(f'El resultado de sumar los impares es {suma}')


if __name__ == "__main__":
    main()
    