/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*/

function esPrimo(n){
    
    if(n===2){
        return `${n} es primo, `
    }

    if(n<2){
        return `${n} no es primo, `
    }
    
    for(let i = 2; i<n; i++){
        if(n%i===0){
            return `${n} no es primo, `
        }
    }
    
    return `${n} es primo, `
}

function fibonacci(n){
    let x = 0;
    let y = 1;
    let z = 1;
    let arr=[]
    
    for (let i = 0; i <= n; i++) {
        z = x + y;
        x = y;
        y = z;
    }

    return x
}

function secuenciaFibonacci(x){
    let secFib = [0,1]
    for(let i = 0; i <= x; i++){
        secFib.push(fibonacci(i))
    }
    return secFib
}

function esFibonacci(y){
    if(y===0){
        return `fibonacci `
    }else if(y===1){
        return `fibonacci `
    }else {
        let newArr = secuenciaFibonacci(y)
        if(newArr.includes(y)){
            return `fibonacci `
        }else{
            return `no es fibonacci `
        }
    }
    
}

function esPar(n){
    if(n%2===0){
        return `y es par`
    }else{
        return `y es impar`
    }
}


function esPrimoFibonacciPar(n){
    let mensaje = ""
    mensaje+=esPrimo(n)+esFibonacci(n)+esPar(n)
    return mensaje
}

console.log(esPrimoFibonacciPar(2)) // 2 es primo, fibonacci y es par 
console.log(esPrimoFibonacciPar(7)) // 7 es primo, no es fibonacci y es impar
console.log(esPrimoFibonacciPar(6)) // 6 no es primo, no es fibonacci y es par