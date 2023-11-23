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


const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

async function weatherCondition (){
    let temp = Number(await getTemp())
    let rain = Number(await getRain())
    const days = Number(await getDays())
    let maxTemp = temp
    let minTemp = temp
    let rainDays = 0
    
    for (let i=0; i<days; i++){
        if (rain=== 100) rainDays++
        console.log(`Day ${i+1}: ${temp}°C, ${(rain=== 100) ? 'Is raining': 'Is not raining'}, (${rain}%)`)
        if (temp> maxTemp) maxTemp = temp
        if (temp< minTemp) minTemp = temp        
        const changeTemp = Math.floor(Math.random() * 100)        
        if (changeTemp >= 90){
            temp = (Math.random()< 0.5) ? temp+2 : temp-2           
        }
        if (temp >= 25) rain+=20 
        else if (temp < 5) rain -= 20

        if (rain >= 100){
            temp--            
            rain = 100
        } else if (rain <= 0) rain=0
    }
    console.log(`MaxTemp: ${maxTemp}, MinTemp: ${minTemp}, Days raining: ${rainDays}`)
    rl.close()
}


weatherCondition()


function getTemp(){
    return new Promise((resolve, reject) => {
        rl.question('Please enter the initial temperature: ', async (answer)=> {
           if (isNaN(answer)) {
            console.log('Please enter a valid number')
            getTemp().then(resolve)
            } else {
                resolve(answer)
            }
        })
    })
}

function getRain(){
    return new Promise((resolve, reject) => {
        rl.question('Please enter the rain probability: ', async (answer)=> {
            if (isNaN(answer)) {
                console.log('Please enter a valid number')
                getRain().then(resolve)
            } else {
                resolve(answer)
            }
        })
    })
}

function getDays(){
    return new Promise((resolve, reject) => {
        rl.question('Please enter the days you want to predict: ', async (answer)=> {
            if (isNaN(answer)) {
                console.log('Please enter a valid number')
                getDays().then(resolve)
            } else {
                resolve(answer)
            }
        })
    })
}
