/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reto3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();

            Console.WriteLine("Cuantos caracteres quieres que tenga tu contraseña (entre 8 y 16): ");
            int size = int.Parse(Console.ReadLine());

            Console.WriteLine("Quieres que tenga caracteres en mayuscula (S/N): ");
            bool mayus = Console.ReadLine().ToUpper() == "S";

            Console.WriteLine("¿Quieres que contenga numeros? (S/N) ");
            bool number = Console.ReadLine().ToUpper() == "S";

            Console.WriteLine("¿Quieres que contenga simbolos? (S/N) ");
            bool symbol = Console.ReadLine().ToUpper() == "S";

            // Llamar a la función creationchainrandom y pasarle los parámetros necesarios
            string chainrandom = creationchainrandom(size, random, mayus, number, symbol);

            // Resto del código...
        }

        static string creationchainrandom(int size, Random random, bool mayus, bool number, bool symbol)
        {
            // Definir los caracteres permitidos basados en las preferencias del usuario
            string caracteresPermitidos = "abcdefghijklmnopqrstuvwxyz";

            if (mayus)
            {
                caracteresPermitidos += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            }

            if (number)
            {
                caracteresPermitidos += "0123456789";
            }

            if (symbol)
            {
                // Agrega los símbolos que desees incluir
                caracteresPermitidos += "!@#$%^&*()-_+=<>?/";
            }

            char[] resultado = new char[size];
            for (int i = 0; i < size; i++)
            {
                // Seleccionar un carácter aleatorio de la lista de caracteres permitidos
                resultado[i] = caracteresPermitidos[random.Next(caracteresPermitidos.Length)];
            }
            Console.WriteLine(resultado);

            return new string(resultado);
        }
    }
 }