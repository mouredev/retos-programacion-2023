/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */

function weather_simulator(dias, temperatura_inicial, probabilidad_lluvia){
    if(dias < 1) return "El número de días debe ser mayor que 0";
    let temperatura_max = temperatura_inicial;
    let temperatura_min = temperatura_inicial;
    let llueve = false;
    
    for(let i=0; i<dias; i++){
        let probabilidad = Math.floor(Math.random() * 100) + 1;
        if(probabilidad <= 10){
            let cambio = Math.floor(Math.random() * 2) + 1;
            if(cambio == 1){
                temperatura_inicial += 2;
            }else{
                temperatura_inicial -= 2;
            }
        }
        if(temperatura_inicial > 25){
            probabilidad_lluvia += 20;
        }else if(temperatura_inicial < 5){
            probabilidad_lluvia -= 20;
        }
        if(probabilidad_lluvia > 100){
            probabilidad_lluvia = 100;
        }else if(probabilidad_lluvia < 0){
            probabilidad_lluvia = 0;
        }
        if(probabilidad <= probabilidad_lluvia){
            temperatura_inicial -= 1;
            llueve = true;
        }
        if(temperatura_inicial > temperatura_max){
            temperatura_max = temperatura_inicial;
        }else if(temperatura_inicial < temperatura_min){
            temperatura_min = temperatura_inicial;
        }
    }
    if(llueve){
        return `La temperatura máxima es ${temperatura_max}°C, la mínima es ${temperatura_min}°C y va a llover ${dias} días`;
    }

    return `La temperatura máxima es ${temperatura_max}°C, la mínima es ${temperatura_min}°C y no va a llover`;
}

console.log(weather_simulator(7, 20, 50));