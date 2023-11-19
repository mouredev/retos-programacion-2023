using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */
namespace EjercicioMoud
{
	public class Reto40
	{
		public static void Main(string[] args)
		{

			string? numeroLeido = null;

			int numero;

			bool seguir = true;

			int numMin = 1;
			int numMax = 10;

			do
			{

				Console.WriteLine($"Escribe un numero entre el {numMin} y el {numMax}, 0 para salir");

				numeroLeido = Console.ReadLine();

				if (int.TryParse(numeroLeido, out numero))
				{

					if (numero == 0) seguir = false;
					else
					{
						if (numero >= numMin && numero <= numMax)
						{

							for (int i = 1; i < 11; i++)
							{

								Console.WriteLine($"{numero} * {i} = {numero * i}");

							}

							Console.WriteLine("\n");

						}else Console.WriteLine("Escriba un numero que se encuentre en el rango");
					}

				}
				else
				{

					Console.WriteLine("Por favor escriba un numero valido");

				}


			} while (seguir);

		}

	}
}
