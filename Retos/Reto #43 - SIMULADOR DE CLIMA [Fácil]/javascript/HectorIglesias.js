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
let temperatura_max = 0
let temperatura_min = 0
let dia = 0
let dias_lloviendo = 0

function calcular_clima (temperatura, prob_lluvia, numero_dias){
    if (temperatura > temperatura_max){
        temperatura_max = temperatura
    }

    if(dia == 0){
        temperatura_min = temperatura
    }
    else{
        if(temperatura < temperatura_min){
            temperatura_min = temperatura
        }
    }

    if(numero_dias > 0){
        dia += 1
        console.log("El dia " +dia+ " habrá " +temperatura+ " grados con " +prob_lluvia+ "% de lluvia")
        let llueve = false
        if (prob_lluvia == 100){
            llueve = true
            temperatura -= 1
            dias_lloviendo += 1
        }
        
        let prob_temperatura_cambie= Math.floor(Math.random() * 100)
        if (prob_temperatura_cambie < 10){
            if(Math.floor(Math.random()) == 0){
                temperatura += 2
            }
            else{
                temperatura -= 2
            }
        }

        if (temperatura => 25){
            if (prob_lluvia < 100){
                prob_lluvia += 20
            }  
        }

        if (temperatura < 5){
            prob_lluvia -= 20
        }
    
        numero_dias -= 1
        calcular_clima(temperatura, prob_lluvia, numero_dias)
    } 
}

calcular_clima(26, 0, 10)
console.log("La temperatura máxima ha sido "+temperatura_max)
console.log("La temperatura mínima ha sido "+temperatura_min)
console.log("Ha llovido "+dias_lloviendo+" días")