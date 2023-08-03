/*
    Generador pseudoaleatorio:
    Mi solución se basa en realizar operaciones usando las unidades de tiempo
    para generar números pseudoaleatorios.
    
    El generador tomará los valores de minuto, segundo y milisegundo actuales. 
    Teniendo estos datos, el número a generar (X) sigue la siguiente fórmula:

    X = m * s * ms * sqrt(ms)
    donde:
        m: minuto
        ms: milisegundos
        s: segundo
    
    Esta operación nos retornará un número positivo real. 

                        Ej: 77.04889751979387

    Dado que nos interesa un valor entre 0-100, vamos a considerar únicamente 
    los valores decimales, para ello, restaremos el valor entero quedándonos únicamente
    la parte decimal. 

                   77.04889751979387 - 77 = 0.04889751979387

    Ahora, de este resultado nos interesará únicamente sus dos primeros dígitos por lo cual 
    multiplicaremos por 100 y truncamos el número a su parte entera. Hecho esto garantizamos 
    que el número obtenido siempre estará entre el rango establecido (0-100)

                    0.04889751979387 * 100 = 4.889751979387
                                     4
        

*/

function getValues() {
    const currentDate = new Date()
    const milliseconds = currentDate.getMilliseconds()
    const seconds = currentDate.getSeconds()
    const minutes = currentDate.getMinutes()

    return {ms:milliseconds, s:seconds, m:minutes}
}

function numberGenerator() {
    const values = getValues()

    X = Math.abs(
            ((values.m * values.s * values.ms) / Math.sqrt(values.ms)) 
        )
    
    const generatedNumber = Math.trunc((X - Math.trunc(X)) * 100)
    
    return generatedNumber
}

// Puesto que la implementación usa unidades de tiempo, es necesario
// realizar esperas entre generación, para garantizar que los números
// sean diferentes. El valor de delay se puede modificar a conveniencia del usuario



const delay = -1
const numOfRandomNumbers = 10
let randomNumbers = []

async function delayedPrint() {
    console.log(`Generando ${numOfRandomNumbers} números pseudoaleatorios ...`)
    for (let i = 0; i < numOfRandomNumbers; i++) {
        const number = numberGenerator()
        randomNumbers.push(number)
        await new Promise(resolve => setTimeout(resolve, delay))
    }
    console.log(`Números pseudoaleatorios generados: ${randomNumbers}`)
}

delayedPrint();








