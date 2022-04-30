class Alumno:
    def __init__(self, nombre, nro_registro) -> None:
        self.nombre = nombre
        self.nro_registro = nro_registro 

    def Display(self):
        print ("El estudiante se llama {self.nombre} y su numero de registro es {self.nro_registro}")
    
    def setAge(self, edad):
        self.edad = edad 

    def setNota (self, nota): 
        self.nota = nota
        notas = []
        notas.append(self.nota)
        print (notas)
