fun drawStaircase(steps: Int) {
    if(steps == 0) {
        println("--")
    } else if(steps > 0) {
        (0..steps).forEach { step ->
            (1..(steps - step)).forEach { _ ->
                print("  ")
            }
            println(if(step == 0) "_" else "_|")
        }
    } else {
        (steps..0).forEach { step ->
            println(if(step == steps) "_" else " |_")
            ((steps - step)..-1).forEach { _ ->
                print("  ")
            }
        }
    }
}

fun main() {
    drawStaircase(10)
    drawStaircase(0)
    drawStaircase(-10)
}