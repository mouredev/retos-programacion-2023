/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 
 namespace LenguajeHacker
{
	class Program
	{
		static void Main(string[] args)
		{
			lenguajeHacker();
			Console.WriteLine("Presiona cualquier tecla para finalizar...");
			Console.ReadKey();
		}

		public static void lenguajeHacker()
		{
			Dictionary<String, String> diccionarioDeCaracteresCambiados = new Dictionary<String, String>(){
				{"A", "4"},
				{"B", "I3"},
				{"C", "["},
				{"D", ")"},
				{"E", "3"},
				{"F", "|="},
				{"G", "&"},
				{"H", "#"},
				{"I", "1"},
				{"J", ",_|"},
				{"K", ">|"},
				{"L", "1"},
				{"M", @"/\/\"},
				{"N", "^/"},
				//He añadido la ñ porque puede ser curioso el resultado sin esta letra :D
				{"Ñ", "Na4" },
				{"O", "0"},
				{"P", "|*"},
				{"Q", "(_,)"},
				{"R", "I2"},
				{"S", "5"},
				{"T", "7"},
				{"U", "(_)"},
				{"V", @"\/"},
				{"W", @"\/\/"},
				{"X", "><"},
				{"Y", "j"},
				{"Z", "2"}
			};

			string cadenaHackeable = Console.ReadLine();



			if(cadenaHackeable == null || cadenaHackeable == "")
			{
				Console.WriteLine("La cadena introducida no es correcta");
				lenguajeHacker();
			}

			string cadenaHackeada = "";

			for(int posicion = 0; posicion <= cadenaHackeable.Length - 1; posicion++)
			{
				foreach (var buscarCaracteres in diccionarioDeCaracteresCambiados)
				{
					if (buscarCaracteres.Key == cadenaHackeable[posicion].ToString().ToUpper())
					{
						cadenaHackeada += buscarCaracteres.Value;
					}
				}
			}
			Console.WriteLine("La cadena con LEGUAJE HACKER es: " + cadenaHackeada);
		}
		
	}
}
 
