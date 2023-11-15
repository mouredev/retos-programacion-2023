/*
 * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
 * de un lugar ficticio al pasar un número concreto de días según estas reglas:
 * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
 * - Cada día que pasa:
 *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
 *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
 *     siguiente aumenta en un 20%.
 *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
 *     siguiente disminuya en un 20%.
 *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
 * - La función recibe el número de días de la predicción y muestra la temperatura
 *   y si llueve durante todos esos días.
 * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
 */

using System;

namespace reto_43
{
    public class Reto43
    {
        static void Main(string[] args)
        {
            string cadena;

            Console.Write("¿De cuantos días quieres la predicción?");
            cadena = Console.ReadLine();

            if (Int32.TryParse(cadena.Trim(), out int num_dias))
            {
                Clima(num_dias);
            }

            Console.ReadKey();
        }

        private static void Clima(int num_dias)
        {
            int temperatura, prob_lluvia;
            string cadena;

            Console.Write("Introduce la temperatura:");
            cadena = Console.ReadLine();
            
            if (Int32.TryParse(cadena.Trim(),out temperatura))
            {
                Console.Write("Introduce la la probabilidad de lluvia:");
                cadena = Console.ReadLine();

                if (Int32.TryParse(cadena.Trim(),out prob_lluvia))
                {
                    Random random = new Random();
                    int temperatura_maxima = 0, temperatura_minima = 100, dias_lloviendo = 0;

                    Console.WriteLine($"Temperatura: {temperatura}");
                    Console.WriteLine($"Probabilidad de lluvia: {prob_lluvia}");

                    for (int i = 0; i < num_dias; i++)
                    {                        
                        if (random.Next(1, 10) == 1)
                        {
                            if (random.Next(0, 1) == 0)
                                temperatura += 2;
                            else
                                temperatura -= 2;
                        }

                        if (temperatura > 25)
                        {
                            if (prob_lluvia <= 80)
                                prob_lluvia += 20;
                            else
                                prob_lluvia = 100;
                        }

                        if (temperatura < 5)
                        {
                            if (prob_lluvia <= 20)
                                prob_lluvia -= 20;
                            else
                                prob_lluvia = 0;
                        }

                        if (prob_lluvia == 100)
                            temperatura--;

                        if (temperatura_maxima < temperatura)
                            temperatura_maxima = temperatura;

                        if (temperatura_minima > temperatura)
                            temperatura_minima = temperatura;

                        if (prob_lluvia == 100)
                            dias_lloviendo++;

                        Console.WriteLine($"Día {i + 1}:");

                        Console.WriteLine($"Temperatura: {temperatura}");
                        Console.WriteLine($"Probabilidad de lluvia: {prob_lluvia}");
                    }

                    Console.WriteLine($"La temperatura máxima ha sido de {temperatura_maxima} grados y la mínima de {temperatura_minima} grados");
                    Console.WriteLine($"Va a llover {dias_lloviendo} días");
                }
            }
        }
    }
}