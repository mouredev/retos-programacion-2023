/*
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */

function program(){
    
    const array_part = ["Pepe", "Julio"]
    let aux = true

    console.log("Bienvenido. A continuación te mostramos las acciones posibles")
    
    while(aux){
        console.log("1. Añadir participante")
        console.log("2. Borrar participante")
        console.log("3. Mostrar participantes")
        console.log("4. Lanzar sorteo")
        console.log("5. Salir")
        let respuesta = prompt("¿Qué deseas hacer? ")
        respuesta = parseInt(respuesta)

        if(respuesta == 1) add(array_part)
        else if (respuesta == 2) erase(array_part)
        else if (respuesta == 3) show(array_part)
        else if (respuesta == 4) sorteo(array_part)
        else if (respuesta == 5){
            aux = false
        }
    }
    
}

function add(array_part){
    let respuesta = prompt("Escriba el nombre del participante: ")

    
    if(array_part.includes(respuesta)){
        console.log("Este participante ya existe, introduzca otro nombre")
        add(array_part)
    }
    else{
        array_part.push(respuesta)
    }
}

function erase(array_part){
    let respuesta = prompt("Escriba el nombre del participante: ")

    if(array_part.includes(respuesta)){
        let index = array_part.indexOf(respuesta)
        array_part.splice(index, 1) 
    }
    else{
        console.log("Este participante no existe. Introduzca otro nombre.")
        erase(array_part)
    }
}

function show(array_part){
    for(let i=0; i<array_part.length; i++){
        console.log((i+1)+". "+array_part[i])
    }
}

function sorteo(array_part){
    let random = Math.floor(Math.random() * array_part.length)

    console.log(array_part[random])
}

program()