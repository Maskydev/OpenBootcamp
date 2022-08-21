''' En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

- Color
- Ruedas
- Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

- Velocidad
- Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.'''

class Vehiculo:
    color = "blanco"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 20
    cilindrada = 1500

miCoche = Coche()
print("mi coche es de color", miCoche.color)
print("mi coche tiene", miCoche.ruedas, "ruedas")
print("mi coche tiene", miCoche.puertas, "puertas")
print("mi coche circula a", miCoche.velocidad)
print("mi coche tiene una cilindrada de", miCoche.cilindrada)