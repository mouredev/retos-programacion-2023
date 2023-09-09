/*
 * Crea un programa que sea capaz de generar e imprimir todas las 
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso 
 */


string word = "";

char? letterI;
char? letterJ;

string wordI = "";
string wordJ = "";


bool follow = true;


List<string> words = new List<string>();
EventArgs eventoEs = new EventArgs();

while (follow)
{

	/* Mejora
	 * if (Console.KeyAvailable)
	{
		var key = Console.ReadKey(true).Key;
		if (key == ConsoleKey.Escape)
		{
			follow = false;
			Console.WriteLine("Saliendo...");

		}
		else if ((key == ConsoleKey.Enter)) { permutaciones(word); word = ""; }

		else if (
			((int)key >= 65 && (int)key <= 90) || ((int)key == 192)) Console.Write(key); word += key;

	}*/

	word = Console.ReadLine();
	permutaciones(word);

}


void permutaciones(string word)
{

	if (word.Length > 1)
	{

		for (int i = 0; i < word.Length; i++)
		{

			letterI = word.ToCharArray()[i];

			wordI = word.Remove(i, 1);

			for (int j = 0; j < wordI.Length; j++)
			{

				letterJ = wordI.ToCharArray()[j];

				wordJ = String.Concat(letterI, letterJ, wordI.Remove(j, 1));

				if (!words.Exists(find => find == wordJ)) words.Add(wordJ);
			}

		}
	}
	else if (word.Length == 1) words.Add(word);

	Console.WriteLine($"\nLas permutaciones obtenidas con la palabra {word} han sido :");

	foreach (var item in words)
	{

		Console.WriteLine($"- {item}");

	}

	Console.WriteLine("\n");

	words.Clear();
}
