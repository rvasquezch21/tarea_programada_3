# Importes del Programa
from persona import Persona
from cola_prioridad import ColaPrioridad

# Definimos y llamamos a la Clase de Cola Prioridad
cola = ColaPrioridad()

# Definimos personas para probar la cola
persona1 = Persona("Juan", "Perez", "Lopez", 70)
persona2 = Persona("Pablo", "Colindres", "Medina", 23)
persona3 = Persona("Maria", "Garcia", "Rodriguez", 60)
persona4 = Persona("Carlos", "Martinez", "Lopez", 80)
persona5 = Persona("Ana", "Sanchez", "Gomez", 65)
persona6 = Persona("Vanessa", "Maria", "Naranjo", 93)
persona7 =Persona("Ana", "Sanchez", "Gomez", 78)

# Insertamos 5 personas en la Cola
cola.enqueue(persona1) 
cola.enqueue(persona2) 
cola.enqueue(persona3)
cola.enqueue(persona4) 
cola.enqueue(persona5) 

# Mostramos el estado de la Cola
cola.imprimir()
print("==========================================")

# Eliminamos una persona de la Cola
cola.dequeue()
# Mostramos el estado de la Cola
cola.imprimir()
print("==========================================")

# Agregamos 2 personas mas a la Cola
cola.enqueue(persona6) 
cola.enqueue(persona7)  

# Eliminamos una persona de la Cola
cola.dequeue()

# Mostramos el estado de la Cola
cola.imprimir()