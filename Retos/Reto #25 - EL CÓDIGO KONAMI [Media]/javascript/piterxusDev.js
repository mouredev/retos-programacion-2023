/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

let readline = require('readline');

readline.emitKeypressEvents(process.stdin);

if (process.stdin.isTTY)
    process.stdin.setRawMode(true);
let test = []
let konami = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a']
console.log("Introduce el código (10 caracteres): ")
process.stdin.on('keypress', (chunk, key) => {
    test.push(key.name)
   
    console.log(key.name)

    if (test.length === 10) {
        if (test.toString() === konami.toString()) {
            console.log('¡Conseguido!')
            console.log(test.toString())
            process.exit();
        } else {
            console.log('El código es incorrecto. Vuelve a intentarlo: ')
            test = []
        }
    }
});

