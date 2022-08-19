# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

# 1-Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
# 2-Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
# 3-Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
# 4-El año es un año bisiesto (tiene 366 días).
# 5-El año no es un año bisiesto (tiene 365 días).


def bisiesto (year):
    esBisiesto = False
    if (year % 4 == 0): #paso 1
        if (year % 100 == 0): #paso 2
            if (year % 400 == 0): #paso 3
                esBisiesto = True #paso 4
                return esBisiesto
            else:
                return esBisiesto #paso 5
        else:
            esBisiesto = True #paso 4
            return esBisiesto 
    else:
        return esBisiesto #paso 5
    
    


year = int(input("Escribe un año: "))

if bisiesto(year):
    print(year, "es bisiesto.")
else:
    print(year, "no es bisiesto.")
