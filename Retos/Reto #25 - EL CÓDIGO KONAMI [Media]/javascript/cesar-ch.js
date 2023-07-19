/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */

const konamiCode = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown", "ArrowLeft", "ArrowRight", "ArrowLeft", "ArrowRight", "KeyB", "KeyA"];
let i  = 0

document.addEventListener("keydown", (e) => {
    e.code === konamiCode[i] ? i++ : i = 0;
    if (i === konamiCode.length) {
        console.log("🎉 GANASTE 🎉")
        i = 0
    }

});