# Importes del Programa
from nodo_lista_sencilla import Nodo

# Definimos la clase de la Cola de Prioridad
class ColaPrioridad:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    # Definimos la funcion para agregar personas a la Cola
    def enqueue(self, persona):
        """
        Inserta una persona en la cola de prioridad.
        Las personas mayores de 65 años se insertan al frente,
        ordenadas de mayor a menor edad.
        """
        nuevo_nodo = Nodo(persona)

        # Definimos la prioridad de la Cola para personas de o mayores a 65 años
        if persona.edad > 64:
            if not self.cabeza or self.cabeza.persona.edad < persona.edad:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
            else:
                # Si ya hay personas mayores de 65, se insertan por edad descendente
                actual = self.cabeza
                while actual.siguiente and actual.siguiente.persona.edad > persona.edad:
                    actual = actual.siguiente
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
        else:
            # Si la persona tiene 65 años o menos, se inserta al final de la cola
            if not self.cabeza:
                self.cabeza = nuevo_nodo
            else:
                actual = self.cabeza
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo_nodo

        self.tamano += 1

    # Definimos la funcion para sacar personas de la Cola
    def dequeue(self):
        """
        Elimina y devuelve la persona al frente de la cola.
        """
        if not self.cabeza:
            print("La cola está vacía.")
            return None

        persona = self.cabeza.persona
        self.cabeza = self.cabeza.siguiente
        self.tamano -= 1
        return persona
    
    # Definimos la funcion para imprimir la Cola
    def imprimir(self):
        if not self.cabeza:
            print("La cola está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.persona)
            actual = actual.siguiente
