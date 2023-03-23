let number = 1;

for(number; number<=100; number++){
    const multipleOf3 = number % 3 === 0;
    const multipleOf5 = number % 5 === 0;

    if(multipleOf3 && multipleOf5){
        console.log("Fizzbuzz");
    }else if(multipleOf3){
        console.log("Fizz");
    }else if(multipleOf5){
        console.log("Buzz");
    }else {
        console.log(number);
    }
}