# README - Tarea 3: Estructuras de Datos
## Introducción
Este proyecto tiene como objetivo implementar y trabajar con diferentes tipos de estructuras de datos, específicamente listas enlazadas y una cola de prioridad. El sistema está diseñado para almacenar y gestionar personas, ordenadas según su edad, y permite realizar varias operaciones como insertar, listar, buscar, y eliminar personas.

### 1. Lista Enlazada Simple
La lista enlazada simple es una estructura de datos en la que cada elemento (o nodo) tiene dos partes:

Un valor (en este caso, una persona).
Un puntero al siguiente nodo.
Cómo funciona:
En esta implementación, los nodos de la lista están ordenados por edad, de menor a mayor. Al insertar una nueva persona en la lista, se recorre la lista desde el principio hasta encontrar la posición correcta según la edad de la persona para insertarla de manera ordenada.

Las principales operaciones que se pueden realizar sobre esta lista son:

Insertar: Se agrega una persona de manera ordenada según su edad.
Imprimir: Se recorre la lista desde el principio y se imprimen las personas en orden.
Buscar: Se pueden buscar personas por edad, nombre o apellido.
Borrar: Se puede eliminar una persona dada su posición en la lista.
Estructura de los nodos:
Cada nodo contiene:

Un valor: una instancia de la clase Persona.
Un puntero al siguiente nodo: referencia al siguiente nodo en la lista, o None si es el último nodo.


### 2. Lista Doblemente Enlazada
La lista doblemente enlazada es similar a la lista enlazada simple, pero con una diferencia clave: cada nodo tiene dos punteros:

Un puntero al siguiente nodo.
Un puntero al nodo anterior.
Esto permite recorrer la lista en ambas direcciones: de la cabeza a la cola y de la cola a la cabeza.

Cómo funciona:
La lista doblemente enlazada se utiliza para almacenar personas, también ordenadas por edad de menor a mayor. La diferencia principal con la lista enlazada simple es que puedes recorrer la lista en ambas direcciones gracias a los punteros anterior y siguiente en cada nodo.

Las principales operaciones son las mismas que en la lista enlazada simple, pero ahora también puedes recorrer la lista en reversa:

Insertar: Se agrega una persona en orden por edad, manteniendo los punteros de los nodos correctamente actualizados.
Imprimir: Se puede imprimir la lista de forma normal o en reversa, aprovechando los punteros anterior y siguiente.
Buscar: Se puede buscar por edad, nombre o apellido.
Borrar: Se puede eliminar una persona por su posición, actualizando los punteros anterior y siguiente.
Estructura de los nodos:
Cada nodo contiene:

Un valor: una instancia de la clase Persona.
Un puntero al siguiente nodo: referencia al siguiente nodo.
Un puntero al nodo anterior: referencia al nodo previo.


### 3. Cola de Prioridad para Personas Mayores de 65 Años
La cola de prioridad es una estructura de datos que sigue el principio FIFO (First In, First Out), pero con la diferencia de que las personas mayores de 65 años tienen prioridad. Esto significa que, al agregar personas a la cola, las personas mayores de 65 años siempre serán insertadas antes que las personas más jóvenes, sin importar el orden de llegada.

Cómo funciona:
Al insertar personas, el sistema verifica si la persona tiene más de 65 años. Si es así, se insertará al principio de la cola (si no hay ninguna persona de mayor edad). Las personas menores de 65 años se insertan después de las personas mayores de 65, siguiendo el orden de llegada.

Insertar: Las personas mayores de 65 años se insertan al principio, respetando el orden descendente por edad dentro de este grupo.
Dequeue: Se elimina a la persona del frente de la cola (FIFO), siempre comenzando con las personas mayores de 65 años si están en el frente.
