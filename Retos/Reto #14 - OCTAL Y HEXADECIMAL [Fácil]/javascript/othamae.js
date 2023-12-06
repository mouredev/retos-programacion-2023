/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */


function fromDecimalToOctal (decimalNumber){
    let modules = []
    let div = decimalNumber
    while (div>8 ){        
        const mod = Math.floor(div)% 8
        modules.push(mod)
        div = div/8
    }
    div = Math.floor(div)
    modules.push(div)
    const res = modules.reverse().join('')
    return res
}

function fromDecimalToHexa (decimalNumber){
    const letters = {
        10: 'A',
        11: 'B', 
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    let modules = []
    let div = decimalNumber
    while (div>16 ){        
        const mod = Math.floor(div)% 16
        if (letters[mod]){
            modules.push(letters[mod])
        } else{
            modules.push( mod)
        }
        div = Math.floor(div)/16
    }
    div = Math.floor(div)
    if (letters[div]){
        modules.push(letters[div])
    } else{
        modules.push( div)
    }
    const res = modules.reverse().join('')
    return res    
}


// TEST

fromDecimalToOctal(95)  
console.log(fromDecimalToOctal(95)) // Solution: 137

fromDecimalToHexa(95)  
console.log(fromDecimalToHexa(95)) // Solution: 5F

fromDecimalToHexa(102)  
console.log(fromDecimalToOctal(102)) // Solution: 146

fromDecimalToHexa(102)  
console.log(fromDecimalToHexa(102)) // Solution: 66

fromDecimalToHexa(206)  
console.log(fromDecimalToOctal(206)) // Solution: 316

fromDecimalToHexa(206)  
console.log(fromDecimalToHexa(206)) // Solution: CE

fromDecimalToHexa(1402)  
console.log(fromDecimalToOctal(1402)) // Solution: 2572

fromDecimalToHexa(1402)  
console.log(fromDecimalToHexa(1402)) // Solution: 57A


