// Escribe un programa que muestre por consola (con un print) los
// números de 1 a 100 (ambos incluidos y con un salto de línea entre
// cada impresión), sustituyendo los siguientes:
// Múltiplos de 3 por la palabra "fizz".
// Múltiplos de 5 por la palabra "buzz".
// Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

const isFizzBuzz = (number:number) => {
    const fizzbuzz = number % 5 === 0 && number % 3 === 0;
    const buzz = number % 5 === 0 && !fizzbuzz;
    const fizz = number % 3 === 0 && !fizzbuzz;
    console.log(fizzbuzz ? 'fizzbuzz' : buzz ? 'buzz' : fizz ? 'fizz' : number);
}
  
const oneToHundred = (n:number=1) =>  {
      if (n > 100) {
         return
      }
      isFizzBuzz(n);
      oneToHundred(n + 1);
  
} 
  oneToHundred()
