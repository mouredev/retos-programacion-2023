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

using System;
using System.Text.RegularExpressions;

namespace retosProgramacion2023
{

    class Program
    {
        static void Main(string[] args)
        {
            TriforceRecursive(10);
        }
        /**
        * Funcion que calcula e imprime la trifuerza de Zelda de form recursiva
        * @param level Nivel de la trifuerza
        * @param currentLevel Nivel actual de la trifuerza (por defecto 0)
        */
        static void TriforceRecursive(int level, int currentLevel = 0)
        {
            if (currentLevel == level * 2)
            {
                return;
            }

            string row;
            int firstLevel = level * 2 - 1;
            int secondLevel = 0;

            if (currentLevel < level)
            {
                row = new string(' ', firstLevel - currentLevel);
                row += PrintPoint(currentLevel);
            }
            else
            {
                secondLevel = currentLevel - level;
                row = new string(' ', (level - secondLevel) - 1);
                row += PrintPoint(secondLevel);
                row += new string(' ', 2 * (level - secondLevel) - 1);
                row += PrintPoint(secondLevel);
            }

            Console.WriteLine(row);

            TriforceRecursive(level, currentLevel + 1);
        }
        /**
         * Función que imprime los puntos de la trifuerza
         * @param level Nivel de la trifuerza
         */
        static string PrintPoint(int level)
        {
            return new string('*', 2 * level + 1);
        }
    }
}