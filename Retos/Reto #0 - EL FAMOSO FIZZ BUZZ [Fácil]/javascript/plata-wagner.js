function fizzBuzz(n){
    for(let i=1; i<=n; i++){
        // I used i%15 insted of i%3==0 && i%5==0 because reduce the expression.
        if(i%15 == 0){
            console.log(i + ' fizzbuzz');
        }else if(i%3 == 0){
            console.log(i + ' fizz');
        }else if(i%5 == 0){
            console.log(i + ' buzz');
        }else{
            console.log(i);
        }
    }
}
fizzBuzz(100);