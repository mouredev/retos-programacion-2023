/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

function randomNumber(
    min = 0,
    max = 100,
    semilla = parseInt(new Date().getTime())
  ) {
    let a = 19810324
    let b = 20171125
    let m = 2 ** 32
  
    let number = (min + ((a * semilla + b) % m)) % (max + 1)
  
    return number
  }
  
  let i = 0
  while (i < 100) {
    i++
    console.log(randomNumber(0, 100, parseInt(new Date().getTime()) + i))
  }
  