/*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */

const readline = require('readline/promises')

const rl = readline.createInterface({
    input:process.stdin,
    output: process.stdout
})

const preguntas = {
    1: "What is the Cosmere?",
    2: "How many planets are in the Cosmere?",
    3: "What is a Shard?",
    4: "Who is Hoid?",
    5: "What is Stormlight?",
    6: "What is Investiture?",
    7: "What is a spren?",
    8: "Who is Kaladin?",
    9: "Who is Dalinar?",
    10: "What is a highstorm?",
    11: "What is Roshar?",
    12: "Who is Vin?",
    13: "What is Allomancy?",
    14: "Who is Elend Venture?",
    15: "What is Feruchemy?",
    16: "Who is Sazed?",
    17: "What is Hemalurgy?",
    18: "Who is the Lord Ruler?",
    19: "What is Scadrial?",
    20: "Who are the Kandra?",
    21: "What are the Ten Essences?",
    22: "Who are the Parshendi?",
    23: "What are Shardblades and Shardplates?",
    24: "Who is Jasnah Kholin?",
    25: "Who are the Knights Radiant?",
    26: "What are the Unmade?",
    27: "Who is Odium?",
    28: "What are the Oathgates?",
    29: "Who are the Heralds?",
    30: "What are the Desolations?"
}

const respuestas = {
    1: "Universe",
    2: "Ten",
    3: "Power",
    4: "Character",
    5: "Energy",
    6: "Magic",
    7: "Entity",
    8: "Character",
    9: "Character",
    10: "Storm",
    11: "Planet",
    12: "Character",
    13: "Magic",
    14: "Character",
    15: "Magic",
    16: "Character",
    17: "Magic",
    18: "Character",
    19: "Planet",
    20: "Species",
    21: "Concepts",
    22: "Species",
    23: "Weapons",
    24: "Character",
    25: "Order",
    26: "Entities",
    27: "God",
    28:"Portals",
    29:"Characters",
    30:"Events"
}
const habitaciones = [  '❔','👻','❔',
                        '❔','❔','❔','❔',
                        '❔','👻','❔','❔',
                        '❔','🍬','❔','❔'
                    ]

const randomRoom = [...habitaciones].sort(() => Math.random() - 0.5)
randomRoom.unshift('🚪')

let ArrayRandomRoom = []
for(let i = 0; i<4; i++){
    const valor = i*4
    ArrayRandomRoom.push([...randomRoom].slice(0+valor,4+valor))
}

console.log(ArrayRandomRoom)

let actualRow=0
let actualColumn=0
let habitacionActual = ArrayRandomRoom[actualRow][actualColumn]
let Norte 
let Sur 
let Este
let Oeste

const moverse = (respuesta) =>{
    let accionNoValida = true
    if(respuesta.toLowerCase()==='norte' && Norte){
        habitacionActual=Norte
        actualRow-=1
        accionNoValida = false
    }
    else if(respuesta.toLowerCase()==='sur' && Sur){
        habitacionActual=Sur
        actualRow+=1
        accionNoValida = false
    }
    else if(respuesta.toLowerCase()==='este' && Este){
        habitacionActual=Este
        actualColumn += 1
        accionNoValida = false
    }
    else if(respuesta.toLowerCase()==='oeste' && Oeste){
        habitacionActual=Oeste
        actualColumn -=1
        accionNoValida = false
    }
    else {
        console.log('Accion no valida')
        accionNoValida = true
    }
    return accionNoValida
}
console.log('\n')
console.log('BIENVENIDO A LA CASA ENBRUJADA!!!, el objetivo es encontrar el caramelo, si no es la habitacion correcta se te haran preguntas de los libros de Brandon Sanderson :3?\n\n')


const House = async() =>{

    while(habitacionActual!=='🍬'){
        console.log('\n')
        

        Norte = ArrayRandomRoom[actualRow-1] && ArrayRandomRoom[actualRow-1][actualColumn] ? ArrayRandomRoom[actualRow-1][actualColumn] : null
        Sur = ArrayRandomRoom[actualRow+1] && ArrayRandomRoom[actualRow+1][actualColumn] ? ArrayRandomRoom[actualRow+1][actualColumn]: null
        Este = ArrayRandomRoom[actualRow][actualColumn+1] ? ArrayRandomRoom[actualRow][actualColumn+1] : null
        Oeste = ArrayRandomRoom[actualRow][actualColumn-1] ? ArrayRandomRoom[actualRow][actualColumn-1] : null
        console.log(`Norte: ${Norte ? 'Disponible':'No hay camino'}, Sur: ${Sur ? 'Disponible':'No hay camino'}, Este: ${Este ? 'Disponible':'No hay camino'}, Oeste: ${Oeste ? 'Disponible':'No hay camino'}\n`)

        var validador = true

        while(validador){

        const respuesta = await rl.question('¿En que direccion quieres moverte?: ')
        validador = moverse(respuesta)

        }
        console.log('\n')
        console.log('Habitacion Actual:' +habitacionActual+'\n')
        
        const Ghost =  habitacionActual === '👻' ? 2 : 1
        let flag=0
        while(flag<Ghost){
            const KeyAsk = Math.floor(Math.random() * (Object.keys(preguntas).length))
            const respuestaAPregunta = await rl.question(`${preguntas[KeyAsk]}\n\n`)
            if(respuestaAPregunta.toLocaleLowerCase()!==respuestas[KeyAsk].toLocaleLowerCase()){
                console.log('\n')
                console.log('Respuesta INCORRECTA, intentalo de nuevo')
                console.log('\n')
            }
            else {
                console.log('\n')
                console.log('Respuesta CORRECTA!!!')
                console.log('\n')
                flag+=1
            }
        }
        
    }
    console.log('Bien hecho!!! Lograste encontrar el caramelo 🍬 y salvado al COSMERE')
    rl.close()
    
}
House()