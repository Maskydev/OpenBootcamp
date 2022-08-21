''' En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha 
del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.'''

from time import localtime

def main():
    horaActual = localtime()
    print("Hora: " ,horaActual.tm_hour,":",horaActual.tm_min)
    if (horaActual.tm_hour >= 19):
        print("Hora de ir a casa")
    else: 
        if (horaActual.tm_min > 0):
            print ("Queda" , (19 - horaActual.tm_hour) - 1, "hora/s y " , 60 -horaActual.tm_min, "minutos de trabajo")
        else:
            print ("Queda" , 19 -horaActual.tm_hour, "hora/s y " , 60 -horaActual.tm_min, "minutos de trabajo")
    
if __name__ == "__main__":
    main()