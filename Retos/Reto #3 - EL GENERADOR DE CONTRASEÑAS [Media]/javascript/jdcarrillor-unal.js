/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

const generateCons = (num = 8, mayus= false,numbers = false, simbolos= false  ) =>{
    (num < 8 )? num = 8 : num > 16 ? num = 16 : num = num 
    let password = ""
    let listchars = []
    for(let i = 33; i<127; i++){
        listchars.push(i)
    }
    const arrsimb = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,58,59,60,61,62,63,64,65,91,92,93,94,95,96,97,123,124,125,126]
    const arrnums = [49,50,51,52,53,54,55,56,57,58,59]
    const arrmayus = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,83,84,85,86,87,88,89,90,91]
    if(!simbolos){
        listchars = listchars.filter(num => {
            return !arrsimb.includes(num)
        })
    }if(!numbers){
        listchars = listchars.filter(num => {
            return !arrnums.includes(num)
        })
    }if(!mayus){
        listchars = listchars.filter(num => {
            return !arrmayus.includes(num)
        })
    }
    // console.log(listchars)
    while (password.length < num){
        random_ascii = Math.floor(Math.random() * listchars.length);
        password += String.fromCharCode(listchars[random_ascii])
    }
    return password 
}

console.log(generateCons(16,true,true,true)) // contraseña con todo 
console.log(generateCons(16,true,true,false)) // nada de simbolos 
console.log(generateCons(12,false,true,false)) // sin mayus ni simbolos, puede tener números 
console.log(generateCons(1)) // sin nada y arreglando el mínimo 
console.log(generateCons(29,false,true,true)) // sin mayus y de maximo 16 
console.log(generateCons(9,false,false,true))

