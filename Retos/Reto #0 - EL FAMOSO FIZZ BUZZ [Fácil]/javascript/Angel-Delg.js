const FizzBuzz = ( limit ) => {
   for(let i = 1; i <= limit; i++){
      if(i % 5 === 0 && i % 3 === 0){
         console.log("FizzBuzz")
         continue
      }
      else if(i % 5 === 0){
         console.log("Buzz")
         continue
      }
      else if(i % 3 === 0){
         console.log("Fizz")
         continue
      }
      console.log(i)
   }
}

FizzBuzz(100)