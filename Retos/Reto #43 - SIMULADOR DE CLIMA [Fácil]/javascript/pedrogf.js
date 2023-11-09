/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuya en un 20%.
 *   0- Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */

function weatherSimulation(predictionsDays, temperature, chanceRain) {
    let maxTemperature = temperature
    let minTemperature = temperature
    let nRainyDays = 0

    for (let d = 0; d < predictionsDays ; d++) {
            
        // Posibilidad de variadión de temperatura por día
        if (Math.floor(Math.random() * 100)<= 10) { 
            if (Math.floor((Math.random() * 2)) === 0) { // si el valor random es 0 la temp baja
                temperature -= 2
            } else { // si el valor no es 0 la temperatura sube
                temperature += 2
            }
        }

        // Aumento de la posibilidad de lluvia si la temperatura es superior a 25º
        if (temperature > 25 && chanceRain <= 80) {
            chanceRain += 20 
        } else if (temperature < 5 && chanceRain >= 20){ // Si es menor de 5º entonces disminuye.
            chanceRain -= 20
        }

        if (temperature > maxTemperature) { maxTemperature = temperature }
        if (temperature < minTemperature) { minTemperature = temperature }
        if (chanceRain === 100) { 
            nRainyDays += 1
            temperature--
        }

        console.log(`Probailidades para el día ${ d + 1 } \n -Temperatura: ${temperature}º. \n -Posibilidad de lluvia ${chanceRain}%.\n`)
    }
    console.log(`Resumen de datos:\n -Temperatura máxima: ${maxTemperature}º.\n -Temperatura mínima: ${minTemperature}º.\n  -Días de lluvia: ${nRainyDays}.`)
}

weatherSimulation(90, 20, 60)