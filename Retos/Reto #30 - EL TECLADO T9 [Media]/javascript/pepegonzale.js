/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */


const teclado_t9 = (bloque_pulsaciones) => {
    const dictionary = [
      [".", ",", "?", "!"],
      ["A", "B", "C"],
      ["D", "E", "F"],
      ["G", "H", "I"],
      ["J", "K", "L"],
      ["M", "N", "O"],
      ["P", "Q", "R", "S"],
      ["T", "U", "V"],
      ["W", "X", "Y", "Z"]
    ]
    const seccion_numeros = bloque_pulsaciones.split("-")
    
    
    for (var i = 0; i < seccion_numeros.length; i++) {
      let num = seccion_numeros[i]
      let zone = num[0] -1 
      let howMany = num.length - 1
      console.log(zone)
      console.log(dictionary[zone][howMany])
      
    }
  }
  
  
  
  teclado_t9("6-666-88-777-33-3-33-888")