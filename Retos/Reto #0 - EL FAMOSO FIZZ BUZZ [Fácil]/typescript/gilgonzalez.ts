function multiplo(num : number, divisor: number): boolean{
    if (num % divisor ===0) {
        return true;
    }
    else  {
        return false
    }
}

for (let i = 1; i <=100; i++){
    if (multiplo(i, 3) && multiplo(i, 5)) {
        console.log('fizzbuzz')
        continue;
    }
    if (multiplo(i, 3)) {
        console.log('fizz')
        continue;
    }
    if(multiplo(i, 5)) {
        console.log('buzz')
        continue;
    }
    console.log(i)
}
