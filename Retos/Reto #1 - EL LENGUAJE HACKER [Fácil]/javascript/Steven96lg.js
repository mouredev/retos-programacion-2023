
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

const leetDict = {
    A: '4',
    B: '8',
    C: '<',
    D: '',
    E: '3',
    F: '',
    G: '6',
    H: '#',
    I: '1',
    J: '_',
    K: '',
    L: '1',
    M: '',
    N: '',
    O: '0',
    P: '',
    Q: '0_',
    R: '2',
    S: '5',
    T: '7',
    U: '',
    V: '/',
    W: '//',
    X: '><',
    Y: '`/,',
    Z: '2'
  }

const leetHacker = (cadena) => {
    let newString = ""
  
    for(let i = 0; i < cadena.length; i++){
      if(leetDict[cadena[i].toUpperCase()]){
        newString += leetDict[cadena[i].toUpperCase()]
      }
      else{
        newString += cadena[i]
      }
    }
    
    return newString
} 

console.log(leetHacker("Hola Mundo! Como estan JJJ"))
