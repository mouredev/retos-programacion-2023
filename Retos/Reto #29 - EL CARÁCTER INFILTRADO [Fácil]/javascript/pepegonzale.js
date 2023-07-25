/* # Reto #29: El carácter infiltrado
#### Dificultad: Fácil | Publicación: 17/07/23 | Corrección: 24/07/23

## Enunciado

```
/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

const caracter_infiltrado = (primera_palabra, segunda_palabra) => {
    const caracteres = []

    if (primera_palabra.length === segunda_palabra.length) {
      for (var i = 0; i < primera_palabra.length; i++) {
        if (primera_palabra[i] !== segunda_palabra[i]) {
          caracteres.push(segunda_palabra[i])
        }
      }
        
    }
  else {
    return "La longitud de ambas cadenas tiene que ser la misma"
  }

    return caracteres;
}



console.log(caracter_infiltrado("Hola mundo", "hola.Mundo"))
console.log(caracter_infiltrado('Me llamo.Brais Moure', 'Me llamo brais moure'));