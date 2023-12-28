

fun main(){

    for (i in 1..100){
        solucion2(i)
    }
}

fun solucion2(numero:Int){
    var word:String=""
    if(numero%3==0) word+="fizz"
    if(numero%5==0) word+="buzz"
    if (word.length>0) println(word) else println(numero)
}