// Dont know if this is the best way to do this, but i think it works.
console.log("Multiplos de 3(Fizz), de 5(Buzz), de ambos(FizzBuzz)");
for (let i = 1; i <= 100; i++) {
    if(i % 3 === 0 & i % 5 === 0) {
        console.log("FizzBuzz");
    }else if(i % 3 === 0) {
        console.log("Fizz");
    }else if(i % 5 === 0){
        console.log("Buzz");
    } else {
        console.log(i);
    }
}