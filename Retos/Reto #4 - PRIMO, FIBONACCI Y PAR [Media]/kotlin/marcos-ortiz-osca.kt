/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

 fun main(args: Array<String>) {
    
    for (i in 1..50) {
        println(isPrimo(i)+isFibonacci(i)+isPar(i))
    }   
       
 }

 fun isPrimo(n:Int):String{

   var check=false
    if(n<=1){
         check=false
    }else{
        check=true
        for (i in 2 until n) {
            if (n % i == 0) check=false
         }
    }

    if(check) return "${n} es primo, "

    return "${n} no es primo, "
 }


 fun isFibonacci(n:Int): String {
    if (n == 0 || n == 1) return "fibonacci"
    var a = 0
    var b = 1
    var c = a + b
    while (c < n) {
        if (c == n) return "fibonacci"
        a = b
        b = c
        c = a + b
    }
    return "no es fibonacci"
 }

 fun isPar(n:Int): String {
    if(n % 2 == 0){
        return " y es par."
    }else{
         return " y es impar."
    }
 }