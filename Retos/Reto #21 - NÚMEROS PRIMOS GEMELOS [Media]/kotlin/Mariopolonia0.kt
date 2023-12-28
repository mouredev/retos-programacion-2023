/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

fun main() {
    reto21()
}

class reto21(){

    init{
        for(q in 1..1000){
            for(p in 2..1000){
                if(numeroPrimos(q) && numeroPrimos(p)){
                    val result =  q - p
                
                    if(result == 2){
                        println("($p,$q)")
                    }
                }
            }
        }
    } 
    
    private fun numeroPrimos(numero: Int): Boolean  {

        var esPrimo = true

        for (contador in 2..(numero - 1)) {
            if (numero.mod(contador) == 0)
                esPrimo = false
        }

        return esPrimo
    }
}
