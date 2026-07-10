import json
import os

ARCHIVO = "datos.json"


def cargar():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as archivo:
        return json.load(archivo)


def guardar(lista):
    with open(ARCHIVO, "w") as archivo:
        json.dump(lista, archivo, indent=4)

def agregar_tarea():

    tareas = cargar()

    nombre = input("\nEscribe la tarea: ")

    proyecto = input("¿A qué proyecto pertenece? ")

    print("\nSelecciona prioridad:")
    print("1. Alta 🔥")
    print("2. Media 🟡")
    print("3. Baja 🟢")

    prioridad = input("Opción: ")

    if prioridad == "1":
        nivel = "Alta"

    elif prioridad == "2":
        nivel = "Media"

    elif prioridad == "3":
        nivel = "Baja"

    else:
        nivel = "Sin prioridad"


    nueva_tarea = {
        "tarea": nombre,
        "proyecto": proyecto,
        "prioridad": nivel
    }


    tareas.append(nueva_tarea)

    guardar(tareas)

    print("\n✅ SAN guardó la misión")


def mostrar_tareas():

    tareas = cargar()

    print("\n===== TAREAS DE SAN =====")

    if len(tareas) == 0:
        print("No hay tareas.")
        return

    for i, tarea in enumerate(tareas):

        print(
            f"{i+1}. {tarea['tarea']} - Prioridad: {tarea['prioridad']}"
        )