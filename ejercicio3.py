"""Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
Experimentación (0,5 Puntos)
Crea algunos alumnos
Prueba a ejecutar el método calificación de cada objeto que has creado"""

class alumno ():
    def __init__ (self,nombre,nota)
        self.nombre = nombre
        self.nota = nota 

    def __str__(self):
        return "el alumno,{},se ha creado con éxito".format( self.nombre = nombre)

    def aprobado(self):
        if (self.nota > 4):
            print ("el alumno ha aprobado")
        else: 
            print ("el alumno ha suspendido")
        
from alumno import*
alumno1 = alumno(Alejandra, 8)
alumno2 = alumno(Pablo,5)
alumno3 = alumno(Sofia,3)


