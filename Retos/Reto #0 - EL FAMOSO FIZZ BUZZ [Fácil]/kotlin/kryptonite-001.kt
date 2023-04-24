fun fizzbuzz(number:Int):String{
    if(number % 3 == 0){
        return "fizz"
    }
    if(number % 5 == 0){
        return "buzz"
    } 
    if((number % 3 == 0)&&(number % 5 == 0)){
        return "fizzbuzz"
    }
    return number.toString()
}

fun main(){
    for(i in 1..100){
       println(fizzbuzz(i))
    }   
}


