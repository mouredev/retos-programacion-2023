/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

function randomNumber()
{
    let date = new Date();
    return date.getTime() % 100
   // console.log(date.getTime() % 100) 

}
console.log("This is a random value:", randomNumber());