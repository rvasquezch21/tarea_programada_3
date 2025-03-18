class Nodo:
    def __init__(self, persona):
        self.persona = persona  # El valor almacenado en el nodo (persona en este caso)
        self.siguiente = None   # Puntero al siguiente nodo
        self.anterior = None    # Puntero al nodo anterior
