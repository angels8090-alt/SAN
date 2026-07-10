import tkinter as tk
import json
import os

ARCHIVO = "datos.json"

# -----------------------------
# Cargar tareas
# -----------------------------
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    return []

# -----------------------------
# Guardar tareas
# -----------------------------
def guardar_tareas():
    with open(ARCHIVO, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

# -----------------------------
# Ordenar tareas (Sincroniza UI y Datos)
# -----------------------------
def ordenar_tareas():
    global tareas
    prioridad_orden = {"Alta": 0, "Media": 1, "Baja": 2}
    
    # Ordenamos la lista global directamente para que los índices coincidan con la Listbox
    tareas = sorted(
        tareas,
        key=lambda t: (
            t.get("completada", False),
            prioridad_orden.get(t["prioridad"], 99)
        )
    )

# -----------------------------
# Agregar tarea
# -----------------------------
def agregar_tarea():
    tarea_texto = entrada.get().strip()
    if tarea_texto == "":
        return

    nueva = {
        "tarea": tarea_texto,
        "prioridad": prioridad.get(),
        "completada": False  # Estado inicial explícito
    }

    tareas.append(nueva)
    ordenar_tareas() # Ordenamos antes de guardar
    guardar_tareas()
    actualizar_lista()
    entrada.delete(0, tk.END)

# -----------------------------
# Eliminar tarea
# -----------------------------
def eliminar_tarea():
    seleccion = lista.curselection()
    if not seleccion:
        return

    indice = seleccion[0]
    tareas.pop(indice) # Ahora el índice de la pantalla coincide con el de la lista

    guardar_tareas()
    actualizar_lista()

# -----------------------------
# Completar tarea
# -----------------------------
def completar_tarea():
    seleccion = lista.curselection()
    if not seleccion:
        return

    indice = seleccion[0]
    tareas[indice]["completada"] = True # Ahora modifica la tarea correcta

    ordenar_tareas() # Reordenamos porque cambió su estado
    guardar_tareas()
    actualizar_lista()

# -----------------------------
# Actualizar lista
# -----------------------------
def actualizar_lista():
    lista.delete(0, tk.END)

    for tarea in tareas:
        if tarea.get("completada", False):
            lista.insert(tk.END, f"✅ {tarea['tarea']}")
            continue

        emoji = "🟡"
        if tarea["prioridad"] == "Alta":
            emoji = "🔴"
        elif tarea["prioridad"] == "Media":
            emoji = "🔵"

        lista.insert(tk.END, f"{emoji} {tarea['tarea']} - {tarea['prioridad']}")
        # Al final de actualizar_lista(), justo debajo del bucle for:
    pendientes = sum(1 for t in tareas if not t.get("completada", False))
    total = len(tareas)
    etiqueta_contador.config(text=f"Pendientes: {pendientes} | Total: {total}")



# =============================
# Inicio de la Aplicación
# =============================

tareas = cargar_tareas()
ordenar_tareas() # Asegura buen orden desde el inicio

ventana = tk.Tk()
ventana.title(" SAN")
ventana.geometry("450x550") # Le damos un poco más de altura

titulo = tk.Label(ventana, text="SAN", font=("Arial", 22, "bold"))
titulo.pack(pady=15)

entrada = tk.Entry(ventana, width=35, font=("Arial", 13))
entrada.pack(pady=10)

prioridad = tk.StringVar()
prioridad.set("Alta")

menu = tk.OptionMenu(ventana, prioridad, "Alta", "Media", "Baja")
menu.pack()

boton = tk.Button(ventana, text="➕ Agregar tarea", command=agregar_tarea)
boton.pack(pady=10)

boton_completar = tk.Button(ventana, text="✔️ Completar tarea", command=completar_tarea)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="🗑 Eliminar tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# --- ETIQUETA DEL CONTADOR ---
etiqueta_contador = tk.Label(
    ventana,
    text="Pendientes: 0 | Total: 0",
    font=("Segoe UI", 10, "bold"),
    fg="#555555" # Un gris oscuro para que sea discreto
)
etiqueta_contador.pack(pady=(5, 0))


lista = tk.Listbox(ventana, width=45, height=15, font=("Arial", 11))
lista.pack(pady=10)

actualizar_lista()
ventana.mainloop()
