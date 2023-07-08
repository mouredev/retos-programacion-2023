/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible!
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 *
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

/**
 * Funcion que calcula e imprime la trifuerza de Zelda de form recursiva
 * @param level Nivel de la trifuerza
 * @param currentLevel Nivel actual de la trifuerza (por defecto 0)
 */
fun triforceRecursive(level: Int, currentLevel: Int = 0) {
    if (currentLevel == level * 2) {
        return
    }
    var row = ""
    val firstLevel = level * 2 - 1
    var secondLevel = 0

    if (currentLevel < level) {
        row = " ".repeat(firstLevel - currentLevel)
        row += printPoint(currentLevel)
    } else {
        secondLevel = currentLevel - level
        row = " ".repeat((level - secondLevel) - 1)
        row += printPoint(secondLevel)
        row += " ".repeat(2 * (level - secondLevel) - 1)
        row += printPoint(secondLevel)
    }

    println(row)

    triforceRecursive(level, currentLevel + 1)
}

/**
 * Función que imprime los puntos de la trifuerza
 * @param level Nivel de la trifuerza
 */
fun printPoint(level: Int): String {
    return "*".repeat(2 * level + 1)
}


fun main(){
    triforceRecursive(7)
}