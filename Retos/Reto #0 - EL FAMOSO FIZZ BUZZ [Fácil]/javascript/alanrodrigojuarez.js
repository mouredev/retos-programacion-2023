// Enunciado
    /*
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    */

    function fizz_buzz(){
        for(let i = 0; i<=100; i++ ){
            if(i % 3 == 0 && i % 5 == 0) console.log("%cfizzbuzz", "color: red");
            else if(i % 3 == 0) console.log("%cfizz", "color: yellow");
            else if(i % 5 == 0) console.log("%cbuzz", "color: orange");
            else console.log(`%c${i}`, "color: gray");
        }
    }

    fizz_buzz();