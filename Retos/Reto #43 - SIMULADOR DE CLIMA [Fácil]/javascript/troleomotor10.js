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
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */
function simuladorclima(dias, temperatura, probabilidad_lluvia){
    let temperatura_maxima = 0;
    let temperatura_minima = temperatura;
    let recuento_dias_lluvia = 0;
    let lluvia = false
    for(let i = 1; i <= dias; i++){
        //Si sale entre 1 y 10 disminuimos la temperatura y si sale entre 11 y 20 aumentamos la temperatura 
        let aumento_temperatura = Math.floor(Math.random() * 100)
        if(aumento_temperatura >= 1 && aumento_temperatura <= 10){
            temperatura -= 2
        }else if(aumento_temperatura >= 11 && aumento_temperatura <= 20){
            temperatura += 2
        }
        //Comprobar si la temperatura actual es la maxima o la minima
        if(temperatura > temperatura_maxima){
            temperatura_maxima = temperatura
        }
        if(temperatura < temperatura_minima){
            temperatura_minima = temperatura
        }
        //Comprobar si hoy llueve
        let numero_probabilidad_lluvia = Math.floor(Math.random() * 100)
        if(numero_probabilidad_lluvia < probabilidad_lluvia){
            lluvia = true;
        }
        //Comprobar si la probabilidad de lluvia del dia siguiente aumenta
        if(temperatura > 25){
            if(probabilidad_lluvia + 20 > 100){
                probabilidad_lluvia = 100
            }else{
                probabilidad_lluvia += 20
            }
        }else if(temperatura < 5){
            if(probabilidad_lluvia - 20 < 0){
                probabilidad_lluvia = 0
            }else{
                probabilidad_lluvia -= 20
            }
        }

        //Imprimimos por pantalla los resultados del dia
        console.log(`La temperatura del dia ${i} sera de ${temperatura} Cº. Lluvia: ${lluvia ? "Si" : "No"}`)

        //Aumentamos la temperatura del siguiente dia si hoy llueve
        if(lluvia == true){
            temperatura -= 1
            recuento_dias_lluvia++
        }
    }
    //Imprimimos por pantalla el resultado final
    console.log(`\nLa temperatura maxima de estos días es de: ${temperatura_maxima}Cº`)
    console.log(`La temperatura minima de estos días es de: ${temperatura_minima}Cº`)
    console.log(`Llovera durante ${recuento_dias_lluvia} dias`)
}