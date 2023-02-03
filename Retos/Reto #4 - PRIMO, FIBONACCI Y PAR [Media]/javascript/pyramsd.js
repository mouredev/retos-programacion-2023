function es_fibonacci(n){
    let a = 0;
    let b = 1;
    while (b < n){
        let varTemp = a;
        a = b;
        b = varTemp + b;
        if (b > n) break;
    }
     return b == n;
}

// console.log(es_fibonacci(9));

function es_parImpar(n){
    return n % 2 === 0;
}

// console.log(es_parImpar(4));

function es_primo(n){
    if (n < 2){
        return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++){
        if (n % i === 0){
            return false;
        }
    }
    return true;
}

// console.log(es_primo(4));

function respuestaFinal(num){
    let res_final = "";
    if (es_primo(num)){
        res_final += "es primo, ";
    }else{
        res_final += "no es primo, ";
    }
    if (es_fibonacci(num)){
        res_final += "es fibonacci, ";
    }else{
        res_final += "no es fibinacci, ";
    }
    if (es_parImpar(num)){
        res_final += "y es par";
    }else{
        res_final += "y no es par";
    }
    return `${num} ${res_final}`;
}

console.log(`${respuestaFinal(3)}`);
