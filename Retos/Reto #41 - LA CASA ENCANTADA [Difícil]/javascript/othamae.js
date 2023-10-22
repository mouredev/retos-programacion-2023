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


const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

game()



// Functions

function game(){
    const [emptyhouse, house, door] =createHouse()
    let position = [...door]
    console.log("Welcome to the riddle Mansion Game")
    console.log(emptyhouse)
    console.log("Which room do you want to explore? ")
    console.log("Please choose a movement: (n/s/e/w) ")

    rl.on('line', async (input) => {
        if (!["n", "s", "e", "w"].includes(input.toLowerCase())) {
            console.log("Please enter a valid movement")
        } else if(!canMove(input.toLowerCase(), position)) {
            console.log("You can't go that way. Please try again")            
        } else {
           await handleMovement(input.toLowerCase(), position, house, emptyhouse)     
        }
        (!finish(house, position))   &&  console.log("Please choose a new movement: (n/s/e/w) ")     
    })
       
}

//const
const riddles = [
    {
        question: "I fly in the night, yet I'm not a bird. What am I?",
        answer: "A bat"
    },
    {
        question: "I have a broom and a pointed hat. Who am I?",
        answer: "A witch"
    },
    {
        question: "I'm a vegetable that becomes a lantern. What am I?",
        answer: "A pumpkin"
    },
    {
        question: "I'm scary and I hide in the dark. What am I?",
        answer: "A ghost"
    },
    {
        question: "I'm a popular costume with fangs and a cape. Who am I?",
        answer: "A vampire"
    },
    {
        question: "I am not alive but I still can knock. What am I?",
        answer: "A skeleton"
    },
    {
        question: "I'm round, orange, and have many seeds inside. What am I?",
        answer: "A pumpkin"
    },
    {
        question: "I'm a group of friends who love to go trick-or-treating. Who are we?",
        answer: "A bunch of monsters"
    },
    {
        question: "I'm a celebration where kids get candies. What am I?",
        answer: "Halloween"
    },
    {
        question: "I'm a creature that howls at the moon. What am I?",
        answer: "A werewolf"
    },
    {
        question: "I'm a popular Halloween dessert that's made of sugar. What am I?",
        answer: "Candy corn"
    },
    {
        question: "I'm a scary story told around a fire. What am I?",
        answer: "A ghost story"
    },
    {
        question: "I'm a hairy creature with eight legs. What am I?",
        answer: "A spider"
    },
    {
        question: "I'm a mystical black bird associated with magic. What am I?",
        answer: "A raven"
    },
    {
        question: "I'm a famous Frankenstein's assistant. Who am I?",
        answer: "Igor"
    },
    {
        question: "I'm a cauldron used for brewing potions. What am I?",
        answer: "A witch's cauldron"
    }
]
// Helper functions
function createHouse(){
    const emptyhouse = [
        ['⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛']
    ]   
    const house = [
        ['⬜','⬜','⬜','⬜'],
        ['⬜','⬜','⬜','⬜'],
        ['⬜','⬜','⬜','⬜'],
        ['⬜','⬜','⬜','⬜']
    ]  
    const door = addElement('🚪',house)
    addElement('🍭',house)  
    addElement('👻',house)  
    addElement('👻',house)  
    emptyhouse[door[0]][door[1]] = '🚪'
    return [emptyhouse, house, door] 
}

function addElement(symbol,house){
    const element =[Math.floor(Math.random() * 4), Math.floor(Math.random() * 4)]  
    house[element[0]][element[1]] === '⬜' 
        ? house[element[0]][element[1]] = symbol 
        : addElement(symbol,house)
    return element
}

async function handleMovement(input, position, house, emptyhouse){
    return new Promise(async (resolve) => {
        goToNewPosition(input, position)
        emptyhouse[position[0]][position[1]] = house[position[0]][position[1]]
        console.log(emptyhouse);
        if (checkIfCandyRoom(house, position)) {
             resolve()
             return
        }
        const [question, answer] = getQuestion()
        await checkIfGhostRoom(house, position)
        await askQuestion(question, answer)
        resolve()
    })
}

function goToNewPosition(input, position){
    if (input === "n") position[0] -= 1    
    if (input === "s") position[0] += 1    
    if (input === "e") position[1] += 1    
    if (input === "w") position[1] -= 1  
}

function canMove( movement, position){   
    return !((movement === "n" && position[0] === 0)
    || (movement === "s" && position[0] === 3)
    || (movement === "e" && position[1] === 3)
    || (movement === "w" && position[1] === 0))
}

function checkIfCandyRoom (house, position){
    if (house[position[0]][position[1]] === '🍭'){
        console.log("Congratulations! You found the dulces room!")
      rl.close()
      return true
    }
    return false
}

function finish(house, position){
    return (house[position[0]][position[1]] === '🍭')
}

async function checkIfGhostRoom(house, position){
    return new Promise(async (resolve) => {
        if (house[position[0]][position[1]] === '👻'){
            console.log("You have to answer two questions to escape the ghost room")  
            const [question, answer] = getQuestion()
            await askQuestion(question, answer)     
        }
        resolve()
    })
   
}

function getQuestion(){
    const ramdom = Math.floor(Math.random() * riddles.length)
    const question = riddles[ramdom].question
    const answer = riddles[ramdom].answer
    riddles.splice(ramdom,1)
    return [question, answer]
}

function askQuestion(question, answer) {
    return new Promise((resolve) => {
      const recursiveQuestion = () => {
        rl.question(question, (userAnswer) => {
          checkAnswer(userAnswer, answer).then((isCorrect) => {
            if (isCorrect) {
              console.log("Congratulations! You are right!")  
              rl.prompt()
              resolve()
            } else {
              console.log("Sorry, you are wrong. Please try again")
              recursiveQuestion()
            }
          })
        })
      }
      recursiveQuestion()
    })
  }
  
function checkAnswer(input, answer) {
    return new Promise((resolve) => {
        (input.toLowerCase() === answer.toLowerCase()) 
        ? resolve(true)
        : resolve(false)        
    })
}

