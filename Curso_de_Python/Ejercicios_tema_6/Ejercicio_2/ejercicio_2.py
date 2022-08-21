'''En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada 
Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para 
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y 
si ha aprobado o no.'''

class Alumno:
    nombre = ""
    nota = 0

    def __init__(self, nombreAlumno):
        self.nombre = nombreAlumno

    def setNombre(self, nombreAlumno):
        self.nombre = nombreAlumno

    def getNombre(self):
        return self.nombre

    def setNota(self, notaAlumno):
        self.nota = notaAlumno

    def getNota(self):
        return self.nota;

    def getAprobado(self):
        if(self.nota >= 5):
            return "aprobado!!"
        else:
            return "suspendido!"

miAlumno = Alumno("oscar")
miAlumno.setNota(5)
print(miAlumno.getNombre() , "ha sacada de nota", miAlumno.getNota() , "por tanto ha", miAlumno.getAprobado())
