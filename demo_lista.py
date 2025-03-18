from lista_enlazada import ListaEnlazadaOrdenada
from persona import Persona

# Función para mostrar el menú y permitir al usuario interactuar con las listas
def menu(lista):
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar persona a la lista")
        print("2. Listar personas")
        print("3. Borrar persona")
        print("4. Buscar persona por edad")
        print("5. Buscar persona por nombre")
        print("6. Buscar persona por apellido")
        print("7. Salir")

        # Solicitar la opción que desea realizar el usuario
        opcion = input("Elige una opción (1-7): ")

        if opcion == '1':
            # Opción 1: Agregar persona a la lista
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            edad = int(input("Edad: "))
            persona = Persona(nombre, apellido1, apellido2, edad)
            lista.insertar(persona)  # Insertamos en la lista enlazada ordenada
            print(f"{persona} ha sido agregada a la lista.")
        
        elif opcion == '2':
            # Opción 2: Listar personas
            lista.imprimir()  # Llamamos al método imprimir de la lista para mostrar todas las personas

        elif opcion == '3':
            # Opción 3: Borrar persona
            if lista.tamano > 0:
                posicion = int(input(f"Introduce el número de ítem (0-{lista.tamano-1}) que deseas borrar: "))
                lista.borrar_por_posicion(posicion)  # Llamamos al método borrar por posición
            else:
                print("La lista está vacía, no se puede borrar ninguna persona.")

        elif opcion == '4':
            # Opción 4: Buscar persona por edad
            edad_buscar = int(input("Introduce la edad de la persona que deseas buscar: "))
            lista.buscar_por_edad(edad_buscar)  # Llamamos al método de búsqueda por edad

        elif opcion == '5':
            # Opción 5: Buscar persona por nombre
            nombre_buscar = input("Introduce el nombre que deseas buscar: ")
            lista.buscar_por_nombre(nombre_buscar)  # Llamamos al método de búsqueda por nombre

        elif opcion == '6':
            # Opción 6: Buscar persona por apellido
            apellido_buscar = input("Introduce el apellido que deseas buscar: ")
            lista.buscar_por_apellido(apellido_buscar)  # Llamamos al método de búsqueda por apellido

        elif opcion == '7':
            # Opción 7: Salir
            print("Saliendo del programa...")
            break  # Salimos del ciclo del menú

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")

# Crear una instancia de la lista enlazada ordenada
lista = ListaEnlazadaOrdenada()

# Ejecutamos el menú
menu(lista)
