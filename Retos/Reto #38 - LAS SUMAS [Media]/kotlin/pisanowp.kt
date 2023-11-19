fun main() {

    /*
    * Reto #38 25/09/2023  LAS SUMAS
    *
    * Crea una función que encuentre todas las combinaciones de los números
    * de una lista que suman el valor objetivo.
    * - La función recibirá una lista de números enteros positivos
    *   y un valor objetivo.
    * - Para obtener las combinaciones sólo se puede usar
    *   una vez cada elemento de la lista (pero pueden existir
    *   elementos repetidos en ella).
    * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
    *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
    *   (Si no existen combinaciones, retornar una lista vacía)
    *
    */

//    val lista = listOf(1, 5, 3)
//    val objetivo = 6

    val lista = listOf(1, 5, 3, 2,4,1)
    val objetivo = 7

    println( "Lista => ${lista}")
    println( "Combinaciones para conseguir $objetivo => ${getCombinaciones(lista, objetivo)}" )

}


fun getCombinaciones(lista: List<Int>, objetivo: Int): List<List<Int>> {

    var combinaciones = mutableListOf<List<Int>>()
    combinaciones.add(lista)

    // Voy a crear una lista de listas con TODAS las posibles combinaciones de números
    combinaciones = getAllCombinaciones(combinaciones)

    // Ahora solo me quedo con aquellas, cuya suma de elementos sea igual al objetivo
    val aux = combinaciones.filter{
        it.sum() == objetivo
    }

    // ... Y quito los duplciados
    val conjuntoDeListas = aux.toSet()
    val listaSinDuplicados = conjuntoDeListas.toList()


    // Devuelvo el resutlado
    return  listaSinDuplicados

}

fun getAllCombinaciones(combinaciones: MutableList<List<Int>>): MutableList<List<Int>> {

    var retornoCombinaciones = mutableListOf<List<Int>>()

    //println ("getAllCombinaciones => ${combinaciones}")


    if (   ( combinaciones.size >= 1 )
        && ( combinaciones[0].size > 2 ) ){
        combinaciones.forEach(){
            retornoCombinaciones.add(it)
            val dummyVariaciones = getCombinacion(it)
            //println(dummyVariaciones)

            dummyVariaciones.forEach(){
                retornoCombinaciones.add(it)
                getAllCombinaciones(mutableListOf<List<Int>>(it)).forEach(){
                    retornoCombinaciones.add(it)
                }

            }
        }

    }

    return retornoCombinaciones

}


fun getCombinacion(lista: List<Int>): List<List<Int>> {

    var combinacion = mutableListOf<Int>()
    var combinaciones = mutableListOf<List<Int>>()


    (0 until   lista.size).forEach() { i ->

        (0 until   lista.size).forEach() { j ->
            if ( i!=j ){
                // Para no tomar el valor guia
                combinacion.add( lista[j])

            }
        }

        combinaciones.add(combinacion)

        combinacion  = mutableListOf<Int>()

    }

    return  combinaciones
}