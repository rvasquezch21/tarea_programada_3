# Importes del Programa
from lista_doblemente_enlazada import ListaDobleOrdenada
from persona import Persona

# Menu del programa que permite al usuario interactuar con las listas
def menu(lista):
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar persona a la lista")
        print("2. Listar personas")
        print("3. Listar personas en reversa")
        print("4. Borrar persona")
        print("5. Buscar persona por edad")
        print("6. Buscar persona por nombre")
        print("7. Buscar persona por apellido")
        print("8. Salir")

        # Solicitamos la opción que desea realizar el usuario
        opcion = input("Elige una opción (1-8): ")

        if opcion == '1':
            # Opción 1: Agregar persona a la lista
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            edad = int(input("Edad: "))
            persona = Persona(nombre, apellido1, apellido2, edad)
            lista.insertar(persona)  # Insertamos la persona en la lista
            print(f"{persona} ha sido agregada a la lista.")
        
        elif opcion == '2':
            # Opción 2: Listar personas
            lista.imprimir()  # Llamamos al método imprimir de la lista para mostrar todas las personas
        
        elif opcion == '3':
            # Opción 3: Listar personas en reversa
            lista.imprimir_reversa()  # Llamamos al método imprimir_reversa de la lista para mostrar las personas en reversa

        elif opcion == '4':
            # Opción 4: Borrar persona
            if lista.tamano > 0:
                posicion = int(input(f"Introduce el número de ítem (0-{lista.tamano-1}) que deseas borrar: "))
                lista.borrar_por_posicion(posicion)  # Llamamos al método borrar por posición
            else:
                print("La lista está vacía, no se puede borrar ninguna persona.")

        elif opcion == '5':
            # Opción 5: Buscar persona por edad
            edad_buscar = int(input("Introduce la edad de la persona que deseas buscar: "))
            lista.buscar_por_edad(edad_buscar)  # Llamamos al método de búsqueda por edad

        elif opcion == '6':
            # Opción 6: Buscar persona por nombre
            nombre_buscar = input("Introduce el nombre que deseas buscar: ")
            lista.buscar_por_nombre(nombre_buscar)  # Llamamos al método de búsqueda por nombre

        elif opcion == '7':
            # Opción 7: Buscar persona por apellido
            apellido_buscar = input("Introduce el apellido que deseas buscar: ")
            lista.buscar_por_apellido(apellido_buscar)  # Llamamos al método de búsqueda por apellido

        elif opcion == '8':
            # Opción 8: Salir
            print("Saliendo del programa...")
            break  # Salimos del ciclo del menú

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 8.")

# Crear una instancia de la lista (simple o doblemente enlazada)
lista = ListaDobleOrdenada()

# Ejecutamos el menú
menu(lista)
