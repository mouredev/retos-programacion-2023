using System;

namespace MiPrograma
{
    class Program
    {
        static void Main(string[] args)
        {
            // Punto 1: Hola, mundo!
            Console.WriteLine("Hola, mundo!");

            // Punto 2: Crea una variable de texto o string
            string miTexto = "¡Hola desde C#!";

            // Punto 3: Crea una variable de número entero
            int miEntero = 42;

            // Punto 4: Crea una variable de número con decimales
            double miDecimal = 3.14;

            // Punto 5: Crea una variable de tipo booleano
            bool miBooleano = true;

            // Punto 6: Crea una constante
            const int MI_CONSTANTE = 10;

            // Punto 7: Usa un if, else if y else
            if (miEntero > 50)
            {
                Console.WriteLine("El número es mayor que 50");
            }
            else if (miEntero < 50)
            {
                Console.WriteLine("El número es menor que 50");
            }
            else
            {
                Console.WriteLine("El número es igual a 50");
            }

            // Punto 8: Crea un Array
            int[] miArray = { 1, 2, 3, 4, 5 };

            // Punto 9: Crea una lista (List en C#)
            System.Collections.Generic.List<string> miLista = new System.Collections.Generic.List<string>
            {
                "Manzana", "Banana", "Naranja"
            };

            // Punto 10: Crea una tupla
            (int, string) miTupla = (1, "Tupla");

            // Punto 11: Crea un set (no aplicable en C# directamente, se logra con HashSet)
            System.Collections.Generic.HashSet<string> miSet = new System.Collections.Generic.HashSet<string>
            {
                "Rojo", "Verde", "Azul"
            };

            // Punto 12: Crea un diccionario (Dictionary en C#)
            System.Collections.Generic.Dictionary<string, string> miDiccionario = new System.Collections.Generic.Dictionary<string, string>
            {
                { "clave1", "valor1" },
                { "clave2", "valor2" }
            };

            // Punto 13: Usa un ciclo for
            for (int i = 0; i < miArray.Length; i++)
            {
                Console.WriteLine(miArray[i]);
            }

            // Punto 14: Usa un ciclo foreach
            foreach (var elemento in miLista)
            {
                Console.WriteLine(elemento);
            }

            // Punto 15: Usa un ciclo while
            int contador = 0;
            while (contador < 3)
            {
                Console.WriteLine("Contador: " + contador);
                contador++;
            }

            // Punto 16: Crea una función sin parámetros que no retorne nada
            void FuncionSinParametros()
            {
                Console.WriteLine("Función sin parámetros");
            }

            // Punto 17: Crea una función con parámetros que no retorne nada
            void FuncionConParametros(int param1, string param2)
            {
                Console.WriteLine("Parámetro 1: " + param1);
                Console.WriteLine("Parámetro 2: " + param2);
            }

            // Punto 18: Crea una función con parámetros que retorne valor
            int FuncionConRetorno(int a, int b)
            {
                return a + b;
            }

            // Punto 19: Crea una clase
            Persona miPersona = new Persona("Juan", 30);

            // Punto 20: Muestra control de excepciones
            try
            {
                int resultado = miEntero / 0;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }
    }

    class Persona
    {
        public string Nombre { get; set; }
        public int Edad { get; set; }

        public Persona(string nombre, int edad)
        {
            Nombre = nombre;
            Edad = edad;
        }
    }
}
