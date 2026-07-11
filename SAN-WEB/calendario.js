let eventos = JSON.parse(localStorage.getItem("eventosSAN")) || [];


function guardarEventos(){

    localStorage.setItem(
        "eventosSAN",
        JSON.stringify(eventos)
    );

}



function agregarEvento(){

    const evento = prompt("¿Qué evento quieres agregar?");


    if(evento === null || evento.trim() === ""){
        return;
    }


    eventos.push({

        id: Date.now(),

        nombre: evento

    });


    guardarEventos();

    mostrarEventos();

}



function mostrarEventos(){

    const lista = document.getElementById("listaEventos");


    if(!lista){
        return;
    }


    lista.innerHTML = "";


    eventos.forEach((evento)=>{


        const li = document.createElement("li");


        li.innerHTML = `

            📌 ${evento.nombre}

            <button onclick="eliminarEvento(${evento.id})">

                🗑️

            </button>

        `;


        lista.appendChild(li);


    });


}



function eliminarEvento(id){


    eventos = eventos.filter((evento)=>{

        return evento.id !== id;

    });


    guardarEventos();

    mostrarEventos();


}



mostrarEventos();