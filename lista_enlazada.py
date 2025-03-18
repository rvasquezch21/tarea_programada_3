from nodo_lista_sencilla import Nodo

# Clase ListaEnlazadaOrdenada: Representa la lista enlazada ordenada por edad
class ListaEnlazadaOrdenada:
    def __init__(self):
        # Inicializamos la lista con la cabeza como None
        self.cabeza = None
        self.tamano = 0  # Variable para mantener el número de elementos en la lista

    def insertar(self, persona):
        # Método para insertar una persona en la lista de manera ordenada por edad (de menor a mayor)
        nuevo_nodo = Nodo(persona)  # Creamos un nuevo nodo con la persona
        if not self.cabeza or self.cabeza.persona.edad > persona.edad:
            # Si la lista está vacía o la cabeza tiene una edad mayor, insertamos al principio
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            # Si no, buscamos la posición correcta para insertarlo (de menor a mayor edad)
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.persona.edad < persona.edad:
                actual = actual.siguiente
            # Insertamos el nuevo nodo después del nodo actual
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamano += 1  # Incrementamos el tamaño de la lista

    def imprimir(self):
        # Método para imprimir todas las personas en la lista y el tamaño
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        print(f"Total de personas en la lista: {self.tamano}")
        while actual:
            print(actual.persona)  # Imprimimos la persona en el nodo actual
            actual = actual.siguiente

    def buscar_por_edad(self, edad):
        # Método para buscar personas por edad
        actual = self.cabeza
        encontrado = False
        while actual:
            if actual.persona.edad == edad:
                print(actual.persona)  # Imprime la persona si la edad coincide
                encontrado = True
            actual = actual.siguiente
        if not encontrado:
            print(f"No se encontró ninguna persona con la edad {edad}.")

    def buscar_por_nombre(self, nombre_buscar):
        # Método para buscar personas por el nombre (subcadena)
        actual = self.cabeza
        encontrado = False
        while actual:
            if actual.persona.contiene_nombre(nombre_buscar):
                print(actual.persona)  # Imprime la persona si el nombre contiene la subcadena
                encontrado = True
            actual = actual.siguiente
        if not encontrado:
            print(f"No se encontró ninguna persona con el nombre que contiene '{nombre_buscar}'.")

    def buscar_por_apellido(self, apellido_buscar):
        # Método para buscar personas por apellido (subcadena)
        actual = self.cabeza
        encontrado = False
        while actual:
            if actual.persona.contiene_apellido(apellido_buscar):
                print(actual.persona)  # Imprime la persona si el apellido contiene la subcadena
                encontrado = True
            actual = actual.siguiente
        if not encontrado:
            print(f"No se encontró ninguna persona con el apellido que contiene '{apellido_buscar}'.")

    def borrar_por_posicion(self, posicion):
        # Método para borrar una persona por su posición (índice)
        if posicion < 0 or posicion >= self.tamano:
            print(f"Índice inválido. La lista tiene {self.tamano} elementos.")
            return

        if posicion == 0:
            # Si la posición es 0 (primer elemento), eliminamos la cabeza
            self.cabeza = self.cabeza.siguiente
        else:
            # Buscamos el nodo anterior al que queremos borrar
            actual = self.cabeza
            for i in range(posicion - 1):
                actual = actual.siguiente
            # Ajustamos el puntero del nodo anterior para eliminar el nodo actual
            actual.siguiente = actual.siguiente.siguiente
        self.tamano -= 1  # Decrementamos el tamaño de la lista
