import * as readline from 'readline';
const CapturarTextoPorConsola = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
//Reto #1: EL "LENGUAJE HACKER"
//Enuciado
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


/**
 * 
 * @param textoAConvertir{string}
 * conveite el texto que le llega como parametro a texto hacker
 */
function convertirTextoAHacker(textoAConvertir:string){
    var leet: { [key: string]: string } = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
    "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
    "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
    "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
    const textoMayuscula:string = textoAConvertir.toUpperCase();
    let textoHacker:string = "";
    for (let i = 0; i < textoMayuscula.length; i++) {
        if(textoMayuscula[i]!= " "){
            textoHacker += leet[textoMayuscula[i]];
        }
    }
    return textoHacker;

}

//funcion anonima auto llamada asi misma
(()=>{
    CapturarTextoPorConsola.question('Ingrese texto: ', (dataIngresadaPorTeclado) => {
        console.log(`El texto hacker es: ${convertirTextoAHacker(dataIngresadaPorTeclado)}`)
      CapturarTextoPorConsola.close();
    });
})()







