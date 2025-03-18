from nodo_lista_doble import Nodo

class ListaDobleOrdenada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0  # Variable para mantener el número de elementos en la lista

    def insertar(self, persona):
        # Método para insertar una persona en la lista de manera ordenada por edad (de menor a mayor)
        nuevo_nodo = Nodo(persona)  # Creamos un nuevo nodo con la persona
        if not self.cabeza or self.cabeza.persona.edad > persona.edad:
            # Si la lista está vacía o la cabeza tiene una edad mayor, insertamos al principio
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza:
                self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            if not self.cola:  # Si la lista estaba vacía, el nuevo nodo es también la cola
                self.cola = nuevo_nodo
        else:
            # Si no, buscamos la posición correcta para insertarlo (de menor a mayor edad)
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.persona.edad < persona.edad:
                actual = actual.siguiente
            # Insertamos el nuevo nodo después del nodo actual
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            if nuevo_nodo.siguiente is None:  # Si lo insertamos al final, actualizamos la cola
                self.cola = nuevo_nodo
        self.tamano += 1  # Incrementamos el tamaño de la lista

    def imprimir(self):
        # Método para imprimir todas las personas en la lista desde la cabeza hasta la cola
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        print(f"Total de personas en la lista: {self.tamano}")
        while actual:
            print(actual.persona)  # Imprimimos la persona en el nodo actual
            actual = actual.siguiente

    def imprimir_reversa(self):
        # Método para imprimir todas las personas en la lista desde la cola hasta la cabeza
        if self.cola is None:
            print("La lista está vacía.")
            return
        actual = self.cola
        print(f"Total de personas en la lista: {self.tamano}")
        while actual:
            print(actual.persona)  # Imprimimos la persona en el nodo actual
            actual = actual.anterior

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
            if self.cabeza.siguiente:
                self.cabeza.siguiente.anterior = None
            self.cabeza = self.cabeza.siguiente
        elif posicion == self.tamano - 1:
            # Si la posición es la última, eliminamos la cola
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        else:
            # Si la posición está en el medio, encontramos el nodo y lo eliminamos
            actual = self.cabeza
            for i in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = actual.anterior
        self.tamano -= 1  # Decrementamos el tamaño de la lista
