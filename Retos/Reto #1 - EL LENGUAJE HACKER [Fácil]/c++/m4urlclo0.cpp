/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

#include <iostream>
#include <string>
#include <map>

std::map<char, std::string> alphabet = {
	{'a', "4"},      {'b', "I3"},
	{'c', "["},      {'d', ")"},
	{'e', "3"},      {'f', "|="},
	{'g', "&"},      {'h', "#"},
	{'i', "1"},      {'j', ",_|"},
	{'k', ">|"},     {'l', "1"},
	{'m', "[]V[]"},  {'n', "^/"},
	{'o', "0"},      {'p', "|*"},
	{'q', "(_,)"},   {'r', "I2"},
	{'s', "5"},      {'t', "7"},
	{'u', "(_)"},    {'v', "|/"},
	{'w', "VV"},     {'x', "><"},
	{'y', "j"},      {'z', "2"},
	{' ', " "}
};

std::string leetHackerAlphabet(std::string Text) {
	std::string _Text = "";
	for (int i = 0; i < Text.length(); i++) {
		_Text += alphabet[tolower(Text[i])];
	}
	return _Text;
}

int main() {
	std::string TextPru = "";
	std::cout << "m4urlclo0 " << char(26) << " " << leetHackerAlphabet("m4urlclo0") << std::endl;
	std::cout << "mouredev  " << char(26) << " " << leetHackerAlphabet("mouredev")  << std::endl;
	std::cout << "\nIngrese un texto de prueba: ";
	std::getline(std::cin, TextPru);
	std::cout << "Texto Ingresado " << char(26) << " " << leetHackerAlphabet(TextPru) << std::endl;
	std::system("pause");
	return 0;
}