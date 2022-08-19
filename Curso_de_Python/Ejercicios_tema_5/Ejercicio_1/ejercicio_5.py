# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función 
# que calcule el área de un círculo recibiendo el radio del mismo.
import math

def areaTriangulo (base, altura):
    return (base * altura)/2

def areaCiruclo(radio):
    return round(math.pi * math.pow(radio, 2), 2)

base= int(input("¿Cual es la base del triangulo? "))
altura= int(input("¿Cual es la altura del triangulo? "))
radio= int(input("¿Cual es el radio del circulo? "))

print(areaTriangulo(base, altura))
print(areaCiruclo(radio))