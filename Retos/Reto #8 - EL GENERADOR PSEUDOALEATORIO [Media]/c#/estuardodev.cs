/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

using System;

class Program
{
    public static void Main(String[] args)
    {
        Console.WriteLine(Pseudoaleatorio());
    }

    public static int Pseudoaleatorio()
    {

        int semilla = DateTime.Now.Millisecond;
        int numeroAleatorio;

        const int a = 48271;
        const int m = 2147483647; // 2^31 - 1

        semilla = (a * semilla) % m;

        numeroAleatorio = semilla % 101;

        return numeroAleatorio;
    }
}