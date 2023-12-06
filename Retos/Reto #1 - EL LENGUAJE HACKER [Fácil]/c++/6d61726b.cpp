#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	const map<char, string> LEET_SPEAK_ALPHABET = {
		{'a', "4",},
        {'b', "I3",},
        {'c', "[",},
        {'d', ")",},
        {'e', "3",},
        {'f', "|=",},
        {'g', "&",},
        {'h', "#",},
        {'i', "1",},
        {'j', ",_|",},
        {'k', ">|",},
        {'l', "1",},
        {'m', "/\\/\\",},
        {'n', "^/",},
        {'o', "0",},
        {'p', "|*",},
        {'q', "(_,)",},
        {'r', "I2",},
        {'s', "5",},
        {'t', "7",},
        {'u', "(_)",},
        {'v', "\\/",},
        {'w', "\\/\\/",},
        {'x', "><",},
        {'y', "j",},
        {'z', "2",},
        {'1', "L"},
        {'2', "R",},
        {'3', "E",},
        {'4', "A",},
        {'5', "S",},
        {'6', "b",},
        {'7', "T",},
        {'8', "B"},
        {'9', "g",},
        {'0', "o"},
        {' ', " "}
	};

	string texto = "";
	getline(cin, texto);

	for (char caracter : texto)
	{
		auto iterador = LEET_SPEAK_ALPHABET.find(caracter);
		if (iterador != LEET_SPEAK_ALPHABET.end())
			cout << iterador->second;
	}

	cout << endl;
	return 0;
}