/**
 * Imprimer los numeros desde un numero inicial que se le proporcione hasta un numero final, reemplazando los siguientes numeros:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz" 
 * @param {Number} init Número del que se iniciará
 * @param {Number} limit Número en donde se detendrá la iteración
 */
const fizzbuzz = (init = 0, limit = 100) => {
    let text = ''
    while (init < limit) {
        init++
        text =
            (init % 15 === 0) ? `fizzbuzz` :
                (init % 3 === 0) ? `fizz` :
                    (init % 5 === 0) ? `buzz` : init
        console.log(text)
    }
}
fizzbuzz()