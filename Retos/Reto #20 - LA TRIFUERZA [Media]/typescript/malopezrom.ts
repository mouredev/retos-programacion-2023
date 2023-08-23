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

import chalk from 'chalk'


/**
 * Funcion que imprime la trifuerza de Zelda de forma recursiva
 * @param level Nivel de la trifuerza
 * @param currentLevel Nivel actual de la trifuerza
 */

function triforceRecursive(level: number, currentLevel: number = 0): void {
    if (currentLevel === level * 2) {
        return;
    }
    let row: string = ""
    const first_level = level * 2 - 1
    let second_level: number = 0

    if (currentLevel < level) {
        row = " ".repeat(first_level - currentLevel)
        row+= chalk.green(printPoint(currentLevel))
    } else {
        second_level = currentLevel - level;
        row = " ".repeat((level - second_level) - 1)
        row+= chalk.red(printPoint(second_level))
        row += " ".repeat(2 * (level - second_level) - 1)
        row+= chalk.red(printPoint(second_level))
    }

    console.log(row);

    triforceRecursive(level, currentLevel + 1)
}


/**
 * Funcion que imprime los puntos de la trifuerza
 * @param level Nivel de la trifuerza
 */
function printPoint(level:number):string{
    return "*".repeat(2 * level + 1)

}


triforceRecursive(7)
