''' En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.'''

import sqlite3


def main():
   bbdd= "ALUMNOS.bd"
   listaAlumnos = [
      ("Juan", "Muñoz"),
      ("Pedro", "Perez"),
      ("Ramon", "Puig"),
      ("Carolina", "Ramos"),
      ("Marta", "Ribas"),
      ("Rosa", "Angulo"),
      ("Juan", "Lindo"),
      ("Eva", "Casas")
   ]


   def createTable():
      conn = sqlite3.connect(bbdd)
      cursor = conn.cursor()
      query = 'CREATE TABLE IF NOT EXISTS Alumno (id int PRIMARY KEY, name TEXT NOT NULL, surname TEXT NOT NULL)'
      cursor.execute(query)
      cursor.close()
      conn.close()

   def searchByName(name):
      conn = sqlite3.connect(bbdd)
      cursor = conn.cursor()
      query = f'SELECT * FROM Alumno WHERE name="{name}"'
      rows = cursor.execute(query)
      data = rows.fetchall()
      print(data)
      cursor.close()
      #conn.close()
      if (data == None):
         print("No hay ningún usuario llamado ", name)
      else:
         resultados = len(data)
         print(f"Se ha encontrado {resultados} usuario/s llamado/s ", name)
         print("Sus id son:")
         for identificador in data:
            print(f"Id: {identificador[0]} Nombre: {identificador[1]} Apellido: {identificador[2]}")

   def insertData(id, name, surname):
      conn = sqlite3.connect(bbdd)
      cursor = conn.cursor()
      query = f'INSERT INTO Alumno(id, name, surname) VALUES({id}, "{name}", "{surname}")'
      cursor.execute(query)
      conn.commit()
      cursor.close()
      conn.close()

   createTable()
   idCreator = 0
   for alumno in listaAlumnos:
      idCreator = idCreator + 1
      insertData(idCreator, alumno[0], alumno[1])

   searchByName('Juan')

if __name__ == "__main__":
    main()