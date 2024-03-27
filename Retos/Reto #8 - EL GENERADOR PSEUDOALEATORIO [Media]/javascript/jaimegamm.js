/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

// Inicialización de variables
let seed = 42;  // Puedes cambiar el valor inicial (semilla)
const a = 1664525;
const c = 1013904223;
const m = 2**32;

// Función para generar números pseudoaleatorios entre 0 y 100
function generarPseudoAleatorio() {
    seed = (a * seed + c) % m;
    return (seed % 101);  // Módulo 101 para obtener valores entre 0 y 100
}

// Ejemplo de uso
for (let i = 0; i < 10; i++) {
    let numeroAleatorio = generarPseudoAleatorio();
    console.log(numeroAleatorio);
}