function fibonacci(numero: number): boolean{
    let secuenciaF : number[]=[0];
    let fActual = 1;
    while(fActual<=numero){
        secuenciaF.push(fActual);
        fActual +=secuenciaF[secuenciaF.length-2]
    }
    if (secuenciaF.includes(numero)) return true
    return false
}
function primo(numero:number):boolean{

    let esPrimo = true;
    let divisor = 2;

    while(divisor <= numero/2){
        if(numero%divisor===0){
            esPrimo = false
        }
        divisor++
    }
    return esPrimo;
}
function par(numero:number):boolean{
    if (numero%2===0) return true
    return false
}

function check(numero:number):void{
    let cadena = '';

    let cadPar = par(numero) ? ' es par':' es impar';
    let cadPrimo = primo(numero) ? ', es primo': ', no es primo'
    let cadFibonacci = fibonacci(numero) ? ' y pertenece a la secuencia de Fibonacci' : ' y no pertenece a la secuencia de Fibonacci'
    cadena = numero + cadPar + cadPrimo + cadFibonacci;
    console.log(cadena)
}
check(233)
