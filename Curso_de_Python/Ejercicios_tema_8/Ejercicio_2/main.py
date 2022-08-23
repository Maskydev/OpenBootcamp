''' En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.'''

import pickle


class Vehiculo:
    color = ""
    motor = ""
    ruedas = 0

    def __init__(self, color, motor, ruedas):
        self.color = color
        self.motor = motor
        self.ruedas = ruedas

    def getColor(self):
        return self.color

def main():
    coche1 = Vehiculo("rojo", "gasolina", 4)
    print(f'coche1 color: {coche1.getColor()}')

    f = open('coche.bin', 'wb')
    pickle.dump(coche1, f)
    f.close()

    f = open('coche.bin', 'rb')
    coche2 = pickle.load(f)
    f.close()

    print(f'coche2 color: {coche2.getColor()}')

if __name__ == "__main__":
    main()

