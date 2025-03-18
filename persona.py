# Clase Persona: Representa a una persona con nombre, apellidos y edad
class Persona:
    def __init__(self, nombre, apellido1, apellido2, edad):
        # Inicializamos los atributos de la persona
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad

    def __repr__(self):
        # Representación de la persona para imprimirla fácilmente (puedes modificarla si lo deseas)
        return f"{self.nombre} {self.apellido1} {self.apellido2}, Edad: {self.edad}"

    def __eq__(self, otra_persona):
        # Método para comparar dos personas por su edad
        return self.edad == otra_persona.edad

    def contiene_nombre(self, nombre_buscar):
        # Método para buscar si el nombre contiene una subcadena
        return nombre_buscar.lower() in self.nombre.lower()

    def contiene_apellido(self, apellido_buscar):
        # Método para buscar si alguno de los apellidos contiene una subcadena
        return apellido_buscar.lower() in self.apellido1.lower() or apellido_buscar.lower() in self.apellido2.lower()
