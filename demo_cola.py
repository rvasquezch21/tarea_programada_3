from persona import Persona
from cola_prioridad import ColaPrioridad

# Crear una instancia de la cola de prioridad
cola = ColaPrioridad()

# Crear algunas personas
persona1 = Persona("Juan", "Perez", "Lopez", 70)
persona2 = Persona("Pablo", "Colindres", "Medina", 23)
persona3 = Persona("Maria", "Garcia", "Rodriguez", 60)
persona4 = Persona("Carlos", "Martinez", "Lopez", 80)
persona5 = Persona("Ana", "Sanchez", "Gomez", 65)
persona6 = Persona("Vanessa", "Maria", "Naranjo", 93)
persona7 =Persona("Ana", "Sanchez", "Gomez", 78)

# Insertamos personas en la cola
cola.enqueue(persona1) 
cola.enqueue(persona2) 
cola.enqueue(persona3)
cola.enqueue(persona4) 
cola.enqueue(persona5) 

# Mostramos el estado de la cola
cola.imprimir()
print("==========================================")

cola.dequeue()
# Mostramos el estado de la cola
cola.imprimir()
print("==========================================")

cola.enqueue(persona6) 
cola.enqueue(persona7)  
cola.dequeue()

# Mostramos el estado de la cola
cola.imprimir()