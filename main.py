from tareas import *

while True:

    print("\n==============================")
    print("        SAN v1.0")
    print("==============================")

    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")
    print("4. Misión del día")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        agregar_tarea()

    elif opcion == "2":
        mostrar_tareas()

    elif opcion == "3":
        print("\nHasta luego Santi 🚀")
        break
    elif opcion == "4":
        mision = input("\n¿Cuál es tu misión de hoy? ")
        print(f"\n🔥 Misión guardada: {mision}")

    else:
        print("\nOpción inválida.")
    