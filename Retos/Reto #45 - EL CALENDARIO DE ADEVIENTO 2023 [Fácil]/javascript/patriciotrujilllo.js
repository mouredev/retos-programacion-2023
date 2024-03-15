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

const readline = require('node:readline/promises')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
let arr = []

async function adviento() {

    const res = await rl.question(`Escoja la accion a realiza\n 
    1-Agregar participante \n 
    2-Eliminar participante \n 
    3-Mostrar participantes\n
    4-Comenzar sorteo\n
    5-Salir\n`)
    console.log(`Escogio la opcion: ${res}`)

    if (res === '1') {
        const person = await rl.question(`Ingrese al participante: `)
        const duplicate = arr.includes(person)
        if (duplicate) {
            console.log(`${person} ya ha existe en la lista`)
        }
        else {
            arr.push(person)
            console.log(`Se agrego a: ${person}`)
        }
        adviento()
    }
    else if (res === '2') {
        const person = await rl.question(`Ingrese el participante a Eliminar: `)
        const exists = arr.includes(person)
        if (exists) {
            arr = arr.filter(word => word !== person)
            console.log(arr)
            console.log(`Se elimino a ${person}`)
        }
        else {
            console.log(`No existe ${person} en la lista`)
        }
        adviento()
    }
    else if (res === '3') {
        let a = 0
        arr.forEach(element => {
            a += 1
            console.log(`${a}-${element}`)
        })
        adviento()
    }
    else if (res === '4') {
        const indice = Math.floor(Math.random() * arr.length)
        console.log(`Se ha escogido a: ${arr[indice]}`)
        arr = arr.filter(win => win !== arr[indice])
        adviento()
    }
    else if (res === '5') {
        rl.close()
    }
    else {
        console.log(`Opcion no valida`)
        adviento()
    }
}
adviento()