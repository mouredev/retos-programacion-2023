/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

let myText = "mi texto de prueba"

function fnLenguajeHacker(myText: string) {
    let myLeet: Map<string, string> = new Map([["A","4"],["E","3"],["I","1"],["O","0"],["U","(_)"]])
    let myTextHack = ""

    myText = myText.toUpperCase()
    
    for(let letra of myText){
        let hack = myLeet.get(letra)
        if(hack){
            myTextHack += hack
        } else{
            myTextHack += letra
        }
    }
    return myTextHack
}

function fnLenguajeHackerV2(myText: string) {
    const myLeet: Record<string, string> = {A:"4",E:"3",I:"1",O:"0",U:"(_)"}
    const myTextHack: string[] = []
    
    for(let letra of myText){
        let hack = myLeet[letra.toUpperCase()]
        myTextHack.push(hack ?? letra) //Esta linea reemplaza todo el condicional anterior   
    }

    return myTextHack.join("")
}

console.log("\n")
console.log( myText )
console.log( fnLenguajeHacker(myText) )
console.log( fnLenguajeHackerV2(myText) )
console.log("\n")