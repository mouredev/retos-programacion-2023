/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
class FizzBuzz{
    private max: number;

    constructor(maxValue: number){
        this.max = maxValue;
    }

    public print(): void {
        let i: number;
        for (i = 1; i <= this.max; i++){
            console.log(this.evaluate(i));
        }
    }

    private evaluate(i: number): any {    
        let retorno: any;

        if (i % 3 === 0 && i % 5 === 0) { 
            retorno = "FizzBuzz";
        } else if (i % 3 === 0) {
            retorno = "Fizz";
        } else if(i % 5 === 0){
            retorno = "Buzz";
        } else {
            retorno = i;
        }

        return retorno;
    }
}

const fizzBuzz = new FizzBuzz(100);
fizzBuzz.print();
