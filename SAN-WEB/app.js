let tareas = [];
function guardarTareas() {
    localStorage.setItem("tareasSAN", JSON.stringify(tareas));
}

function cargarTareas() {
    const datos = localStorage.getItem("tareasSAN");

    if (datos) {
        tareas = JSON.parse(datos);
    }
}

function agregarTarea() {

    const input = document.getElementById("tareaInput");
    const prioridad = document.getElementById("prioridad");

    const texto = input.value.trim();

    if (texto === "") {
        return;
    }

    const nuevaTarea = {
        nombre: texto,
        prioridad: prioridad.value,
        completada: false
    };

   tareas.push(nuevaTarea);

ordenarTareas();

guardarTareas();

mostrarTareas();

input.value = ""; 
}


function ordenarTareas() {

    const orden = {
        "Alta": 1,
        "Media": 2,
        "Baja": 3
    };

    tareas.sort((a, b) => {
        return orden[a.prioridad] - orden[b.prioridad];
    });

}


function mostrarTareas() {

    const lista = document.getElementById("listaTareas");

    lista.innerHTML = "";

    tareas.forEach((tarea, indice) => {

        const li = document.createElement("li");

        let emoji = "🟢";

        if (tarea.prioridad === "Alta") {
            emoji = "❗️";
        }

        if (tarea.prioridad === "Media") {
            emoji = "🟠";
        }


        li.innerHTML = `
            ${emoji} ${tarea.nombre}
            <br>
            <button onclick="completarTarea(${indice})">
                ✅ Completar
            </button>
        `;

        lista.appendChild(li);

    });

}


function completarTarea(indice) {

    tareas[indice].completada = true;

    tareas.splice(indice, 1);

    guardarTareas();

    mostrarTareas();

}
cargarTareas();

document.getElementById("tareaInput").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        agregarTarea();
    }

});

mostrarTareas();
