let number

for( number = 1; number<=100; number++ ){
    
    
    if( number % 3 == 0 && number % 5 == 0){
        console.log("fizzbuzz")
    }else if(number % 5 == 0){
        console.log("buzz")
    }else if( number % 3 == 0){
        console.log("fizz")
    }else{
        console.log(number)
    }
}