
/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuye en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */

function Clima(temperatura, p_lluvia, dias) {
    let max = 0
    let min = Infinity
    let dias_lluvia = 0
    let dia = 1

    while (dia <= dias) {
        if (Math.random() * 100 < 10) Math.random() < 0.5 ? temperatura += 2 : temperatura -= 2
        if (temperatura > 25 && p_lluvia < 1) p_lluvia = (p_lluvia + 0.2).toFixed(1)
        if (temperatura < 5 && p_lluvia > 0) p_lluvia = (p_lluvia - 0.2).toFixed(1)
        if (p_lluvia == 1) {
            temperatura -= 1
            dias_lluvia += 1
        }
        if (temperatura > max) max = temperatura
        if (temperatura < min) min = temperatura
        console.log(p_lluvia)
        console.log(`El dia ${dia} la temperatura es de ${temperatura} ${p_lluvia == 1 ? 'llovio' : 'no llovio'}`)
        dia += 1
    }
    console.log(`La cantidad de dias que llovio fue de ${dias_lluvia}, la temperatura maxima alcanzada es de ${max} y la minima es ${min}`)

}

Clima(24, 0.8, 100)