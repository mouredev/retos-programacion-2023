using System;
				
public class Program
{
	private static void Main(string[] args)
	{
		var text = "Hello, World!!!!!";
		var newText = ConvertToHackerLanguage(text);

		Console.WriteLine($"                          Text: {text}");
		Console.WriteLine($"Text in Hacker language (leet): {newText}");
		Console.ReadLine();
	}

	private static System.Collections.Generic.Dictionary<char, string[]> leetAlphabet = new System.Collections.Generic.Dictionary<char, string[]>() {
		{ 'a', new string[] {"4"} },
		{ 'b', new string[] {"I3"} },
		{ 'c', new string[] {"[", "¢", "{", "<", "(" ,"©"} },
		{ 'd', new string[] {")"} },
		{ 'e', new string[] {"3"} },
		{ 'f', new string[] {"=", "ƒ", "|#", "ph", "/=", "v"} },
		{ 'g', new string[] {"&"} },
		{ 'h', new string[] {"#"} },
		{ 'i', new string[] {"1"} },
		{ 'j', new string[] {",_|"} },
		{ 'k', new string[] {">|"} },
		{ 'l', new string[] {"1"} },
		{ 'm', new string[] { "/\\/\\" } },
		{ 'n', new string[] { "^/" } },
		{ 'o', new string[] { "0"} },
		{ 'p', new string[] { "|*" } },
		{ 'q', new string[] { "(_,)" } },
		{ 'r', new string[] { "I2" } },
		{ 's', new string[] { "5" } },
		{ 't', new string[] {"7" } },
		{ 'u', new string[] { "(_)" } },
		{ 'v', new string[] { "\\/" } },
		{ 'w', new string[] { "\\/\\/" } },
		{ 'x', new string[] { "><" } },
		{ 'y', new string[] { "j"} },
		{ 'z', new string[] { "2"} },
		{ '0', new string[] { "o" } },
		{ '1', new string[] { "L"} },
		{ '2', new string[] { "R"} },
		{ '3', new string[] { "E"} },
		{ '4', new string[] { "A"} },
		{ '5', new string[] { "S"} },
		{ '6', new string[] { "b"} },
		{ '7', new string[] { "T"} },
		{ '8', new string[] { "B"} },
		{ '9', new string[] { "g" } }
	};

	private static string ConvertToHackerLanguage(string text)
	{
		var newText = string.Empty;
		foreach (var character in text.ToLower())
		{
			leetAlphabet.TryGetValue(character, out var value);

			// when a character has not option in leet language, use same character
			if (value == null)
			{
				newText += character;
				continue;
			}

			// when a character has only a option in leet language, use 'value[0]'
			// when a character has many options in leet languagee, use 'RamdonLeet'
			newText += value.Length == 1 ? value[0] : RandomLeet(value);
		}

		return newText;
	}

	private static string RandomLeet(string[] options)
	{
		Random rd = new Random();
		int rand_num = rd.Next(0, options.Length);
		return options[rand_num];
	}
}