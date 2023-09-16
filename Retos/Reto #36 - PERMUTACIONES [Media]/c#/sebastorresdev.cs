/*
# Reto #36: Permutaciones
#### Dificultad: Media | Publicación: 04/09/23 | Corrección: 18/09/23

## Enunciado
*/

/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */

namespace ConsoleApp;

internal class Program
{
    static void Main(string[] args)
    {
        string word = "sol";
        char[] arr = word.ToCharArray();
        GeneratePermutations(arr.Length, arr);
    }

    static void GeneratePermutations(int n, char[] arr)
    {
        if (n == 1) PrintArray(arr);
        else
        {
            for (int i = 0; i < n; i++)
            {
                GeneratePermutations(n - 1, arr);

                if (n % 2 == 0) Swap(ref arr[i], ref arr[n - 1]);
                else Swap(ref arr[0], ref arr[n - 1]);
            }
        }
    }

    static void Swap(ref char a, ref char b) => (b, a) = (a, b);

    static void PrintArray(char[] arr) => Console.WriteLine(string.Join("", arr));
}