/* 
 * ENUNCIADO A RESOLVER
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
*/

const konami_code = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown", "ArrowLeft", "ArrowRight", "ArrowLeft", "ArrowRight", "b", "a"];
let cursor = 0;
document.addEventListener("keydown", (e) => {
    e.key === konami_code[cursor] ? cursor++ : cursor = 0;
    if (cursor === konami_code.length) {
        console.log('Konami!');
        cursor = 0;
    }
});