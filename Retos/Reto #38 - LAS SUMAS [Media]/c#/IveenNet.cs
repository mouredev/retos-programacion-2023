using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
 * Crea una función que encuentre todas las combinaciones de los números
 * de una lista que suman el valor objetivo.
 * - La función recibirá una lista de números enteros positivos
 *   y un valor objetivo.
 * - Para obtener las combinaciones sólo se puede usar
 *   una vez cada elemento de la lista (pero pueden existir
 *   elementos repetidos en ella).
 * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
 *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *   (Si no existen combinaciones, retornar una lista vacía)
 */

namespace EjercicioMoud
{
	public class Reto38
	{

		class ListComparer : IEqualityComparer<List<int>>
		{
			public bool Equals(List<int> x, List<int> y)
			{
				return x.SequenceEqual(y);
			}

			public int GetHashCode(List<int> obj)
			{
				int hashcode = 0;
				foreach (int item in obj)
				{
					hashcode ^= item.GetHashCode();
				}
				return hashcode;
			}
		}


		private static int preguntarLista()
		{

			int numero;

			Console.WriteLine("|Que numero deseas añadir a la lista, escriba 0 para salir|");


			if (int.TryParse(Console.ReadLine(), out numero))
			{

				if (numero < 0)

				{
					Console.WriteLine("--- Escriba un numero positivo ---");
				}


			}
			else { Console.WriteLine("--- Escriba un numero correcto ---"); numero = -1; }


			return numero;

		}

		private static int preguntarNumero()
		{

			int numero;

			Console.WriteLine("Que numero es el objetivo, debe ser mayor que 0");


			if (int.TryParse(Console.ReadLine(), out numero))
			{

				if (numero <= 0)

				{
					Console.WriteLine("--- Escriba un numero positivo o mayor que 0 ---");
				}


			}
			else { Console.WriteLine("--- Escriba un numero correcto ---"); numero = -1; }


			return numero;

		}

		private static string tablasBorrando(ref List<int> cm_listEnteros, ref List<int> cm_listAux, int cm_objetivo)
		{

			List<int> fn_listBorrar = new List<int>();
			string devolver = "";

			cm_listEnteros.Sort((x, y) => y.CompareTo(x));

			while (cm_listEnteros.Sum() >= cm_objetivo)
			{

				cm_listAux.Clear();

				foreach (var item in cm_listEnteros)
				{

					if (cm_listAux.Count == 0)
					{
						if (item > cm_objetivo) { fn_listBorrar.Add(item); } else { cm_listAux.Add(item); }
					}

					else
					{

						if ((cm_listAux.Sum() + item) <= cm_objetivo)
						{
							cm_listAux.Add(item);
						}

					}

				}

				if (cm_listAux.Sum() == cm_objetivo)
				{

					devolver += "[" + string.Join(",", cm_listAux) + "]\n";

					foreach (var item in cm_listAux) cm_listEnteros.Remove(item);

				}

				foreach (var item in fn_listBorrar)
				{
					cm_listEnteros.Remove(item);
				}


			}

			return devolver;

		}
		
		private static void calcular (HashSet<List<int>> cm_resultados, List<int> cm_combinacion, List<int> cm_lista, int cm_objetivo, int cm_item)
		{
			List<int> fn_combinacion = new List<int>(cm_combinacion);
			List<int> fn_pasar;

			for (int i = 0; i < cm_lista.Count; i++)
			{

				if ((cm_combinacion.Sum() + cm_lista.ElementAt(i)) <= cm_objetivo)
				{

					fn_combinacion = new List<int>(cm_combinacion);
					fn_combinacion.Add(cm_lista.ElementAt(i));

					if (fn_combinacion.Sum() == cm_objetivo)
					{
						cm_resultados.Add(fn_combinacion);

					}
					else
					{

						fn_pasar = new List<int>(cm_lista);
						fn_pasar.RemoveRange(0,i+1);

						calcular(cm_resultados, fn_combinacion, fn_pasar, cm_objetivo, cm_lista.ElementAt(i));

					}
				}

			}

		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="args"></param>
		public static void Main(string[] args)
		{
			HashSet<List<int>> resultados = new HashSet<List<int>>(new ListComparer());
			List<int> combinacion = new List<int>();
			List<int> listEnteros = new List<int> { 7, 5, 4, 4, 3, 3, 3, 2, 1, 1, 1 };
			//List<int> listEnteros = new List<int>();
			//List<int> listEnteros = new List<int> { 1,5,3,2 };



			List<int> listAux = new List<int>();

			int numero = 0;
			int objetivo = 10;

			HashSet<List<int>> fn_resultados;
			string mensaje = "";

			do
			{

				/*do
				{

					numero = preguntarLista();

					if (numero > 0) listEnteros.Add(numero);

				} while (numero != 0);

				do
				{

					numero = preguntarNumero();

					if (numero > 0) objetivo = numero;

				} while (objetivo <= 0);*/




				if (listEnteros.Sum() < objetivo)
				{

					Console.WriteLine($"No hay numero en la lista mas grande que el objetivo, resultado es {objetivo}");

				}
				else
				{

					listEnteros.Where(x => (x<=objetivo)).ToList().Sort((x, y) => y.CompareTo(x));

					calcular(resultados, combinacion, listEnteros, objetivo, 0);

					Console.WriteLine($"Todas las combinaciones para sacar el {objetivo} son :\n ");

					foreach (var item in resultados)
					{

						Console.WriteLine($"[{string.Join(",", item)}]");

					}

				}


				listEnteros.Clear();

				Console.ReadKey();

			} while (true);
			
		}		

	}
}
