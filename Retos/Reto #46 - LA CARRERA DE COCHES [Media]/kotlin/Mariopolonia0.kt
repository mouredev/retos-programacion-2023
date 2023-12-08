package EjercicioKotlin.Mouredev

fun main() {
    val meta = "\uD83C\uDFC1"
    val arbol = "\uD83C\uDF32"
    val camino = "_"
    val carroAzul = "\uD83D\uDE99"
    val carroRojo = "\uD83D\uDE97"

    var caminoRecorridoRojo = 10
    var caminoRecorridoAzul = 10


    while (caminoRecorridoRojo > 0 && caminoRecorridoAzul > 0) {

        if ((0..1).random() == 0) {
            caminoRecorridoRojo--
            caminoRecorridoAzul -= 3
        } else {
            caminoRecorridoAzul--
            caminoRecorridoRojo -= 3
        }

        //progreso carro rojo
        println("\n\n\n==================================")

        print(meta)
        if (caminoRecorridoRojo >= 0) {
            for (item in caminoRecorridoRojo downTo 0) {
                print(arbol)
                for (printCamino in 1..4)
                    print(camino)
            }
        }

        print(carroRojo)

        //progreso carro azul
        println()
        print(meta)

        if (caminoRecorridoAzul >= 0) {
            for (item in caminoRecorridoAzul downTo 0) {
                print(arbol)
                for (printCamino in 1..4)
                    print(camino)
            }
        }

        print(carroAzul)

        println("\n==================================")

        Thread.sleep(1000)
    }

    println("\n\n==================================")

    if (caminoRecorridoRojo < caminoRecorridoAzul)
        println("El ganador es el carro Rojo")
    else
        println("El ganador es el carro Azul")

    print("==================================")

}
