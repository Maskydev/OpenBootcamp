''' En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, 
lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.'''

def main():    
    fileName = 'archivo.txt' 
    data = ["Esto es un archivo de prueba", "del ejercicio 1", "del módulo entrada y salida", "de Python", "para practirar la escritura en fichero"]

    f = open(fileName , 'w') 
    f.close()

    f = open(fileName , 'a')
    for line in data:
        if not line.endswith('\n'):
            line = line + '\n'
        f.writelines(line)
    f.close()

if __name__ == '__main__' :
    main()