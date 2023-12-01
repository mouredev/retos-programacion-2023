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

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function aDEViento(){
    console.log("Welcome to aDEViento!!")
    console.log("Please, select an action from the list:")
    console.log("a - Add a participant")
    console.log("r - Remove a participant")
    console.log("s - Show the list of participants")
    console.log("d - Draw the lottery")
    console.log("e - Exit")
    const listOfParticipants = []
    game()
    function game(){       
        rl.question("What do you want to do? ", (answer) => {
            if (answer.toLowerCase() === 'a'){
                rl.question("Please, write the name of the participant: ", (answer) => {
                    if (listOfParticipants.includes(answer.toLowerCase())){
                        console.log("This participant is already in the list")
                    } else {
                        listOfParticipants.push(answer.toLowerCase())
                        console.log("Participant added successfully")
                    }
                    game() 
                })                   
            } else if (answer.toLowerCase() === 'r'){
                rl.question("Please, write the name of the participant to be removed: ", (answer) => {
                    if (!listOfParticipants.includes(answer.toLowerCase())){
                        console.log("This participant is not in the list")
                    } else {
                        const index = listOfParticipants.indexOf(answer.toLowerCase())
                        listOfParticipants.splice(index, 1)
                        console.log("This participant has been removed from the list")
                    }
                    game()
                })       
            } else if (answer.toLowerCase() === 's'){            
                console.log("Here is the list of participants:")
                console.log(listOfParticipants)                
                game()    
            } else if (answer.toLowerCase() === 'd'){
                const randomNumber = Math.floor(Math.random() * listOfParticipants.length)
                const winner = listOfParticipants[randomNumber]
                console.log({randomNumber, winner})
                console.log(`The winner is ${winner}`)
                listOfParticipants.splice(randomNumber, 1)               
                game()    
            } else if (answer.toLowerCase() === 'e'){
                console.log("See you later!!")
                rl.close()
            } else {
                console.log("Please, select a valid option")                
                game()
            }
        })
    }
   
}

aDEViento()