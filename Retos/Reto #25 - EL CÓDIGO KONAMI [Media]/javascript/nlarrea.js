/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

const readline = require('readline');

const konami = [
    'up', 'up',
    'down', 'down',
    'left', 'right',
    'left', 'right',
    'b', 'a'
];

const userPressed = [];

readline.emitKeypressEvents(process.stdin);

if (process.stdin.isTTY) {
    process.stdin.setRawMode(true);
}

console.log('press any key ("ESC" to exit):\n');

process.stdin.on('keypress', (_, key) => {
    if (key && key.name == 'escape') {
        process.exit();
    }

    userPressed.push(key.name);
    console.log(key.name);

    if (userPressed.every((userKey, index) => userKey === konami[index])) {
        console.log('\nKONAMI CODE!\n');
    }

    if (userPressed.length === konami.length) {
        userPressed.shift();
    }
});