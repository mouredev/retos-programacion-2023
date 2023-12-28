
for (let h=1;h <= 100;h++){
    if((h%3)==0 && (h%5)==0){
         console.log(h+"fizzbuzz")
    } else if((h%3)==0){
        console.log(h+"fizz")
    } else if((h%5)==0){
        console.log(h+"buzz")
    } else{
        console.log(h)
    }

}