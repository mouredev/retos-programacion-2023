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

function getMessage(numbers){
    blocks = numbers.split("-");
    message = '';
    character = '';
    for (block of blocks) {
        char = block.charAt(0);
        add = block.length - 1;
        if (!isNaN(block) && (block.match(`[^${char}]`) == null) && (add < 3 || (add == 3 && char == '9'))) {
            switch (char) {
                case '2': character = 'A'; break;
                case '3': character = 'D'; break;
                case '4': character = 'G'; break;
                case '5': character = 'J'; break;
                case '6': character = 'M'; break;
                case '7': character = 'P'; break;
                case '8': character = 'T'; break;
                case '9': character = 'W'; break;
                case '0': character = ' '; break;
                default: console.log("Invalid format!"); return;
            }
        } else {
            console.log("Invalid format!");
            return;
        }
        message += String.fromCharCode(character.charCodeAt(0) + add);
     }
     console.log(message);
     return message;
}

 getMessage("6-2-4-3-444-33-555-0-55-33-999-22-666-2-777-3");