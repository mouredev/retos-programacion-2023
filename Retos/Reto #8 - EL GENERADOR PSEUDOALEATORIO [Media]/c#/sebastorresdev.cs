/*
# Reto #8: El generador pseudoaleatorio
#### Dificultad: Media | Publicación: 20/02/23 | Corrección: 27/02/23

## Enunciado
*/

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

using System.Diagnostics;

int randomNumbers = 20;
Stopwatch sw = Stopwatch.StartNew();
Console.WriteLine("Generador de números aleatorios");

// Generaremos "randomNumbers" numeros aleatorios
for (int i = 0; i < randomNumbers; i++)
    Console.WriteLine(RandomGenerator());
    
int RandomGenerator() => (int)sw.Elapsed.Ticks % 101;