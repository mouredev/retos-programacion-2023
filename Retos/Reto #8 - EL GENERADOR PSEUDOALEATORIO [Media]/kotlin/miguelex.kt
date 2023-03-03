var seed = System.currentTimeMillis().toInt()

fun main() {
        var num: Int
        var a = System.currentTimeMillis().toInt()
        var m = System.currentTimeMillis().toInt() * 1000

        print("¿Cuantos numeros quieres generar?: ")
        num = readLine()?.toInt() as Int

        for (i in 1..num) {
                println("Numero ${i} : ${RandomNumber(a, m) % 100}")
                Thread.sleep(2000)
        }
}

private fun RandomNumber(a: Int, m: Int): Int {
        var q = (a / m).toInt()
        var r = (a % m).toInt()

        seed = a * (seed % q) - r * (seed / q)

        if (seed < 0) {
                seed += m
        }

        return Math.abs(seed)
}
