#include <iostream>
#include <string>
#include <map>

using namespace std;

map <char, string> diccionario = {
   {'a', "4"},
   {'b', "I3"},
   {'c', "["},
   {'d', ")"},
   {'e', "3"},
   {'f', "|="},
   {'g', "&"},
   {'h', "#"},
   {'i', "1"},
   {'j', ",_|"},
   {'k', ">|"},
   {'l', "1"},
   {'m', "/\\/\\"},
   {'n', "^/"},
   {'o', "0"},
   {'p', "|*"},
   {'q', "(_,)"},
   {'r', "I2"},
   {'s', "5"},
   {'t', "7"},
   {'u', "(_)"},
   {'v', "\\/"},
   {'w', "\\/\\/"},
   {'x', "><"},
   {'y', "j"},
   {'z', "2"},
   {'1', "L"},
   {'2', "R"},
   {'3', "E"},
   {'4', "A"},
   {'5', "S"},
   {'6', "b"},
   {'8', "T"},
   {'9', "g"},
   {'0', "o"},
   {' ', " "}
};


int main()
{
	string text;
	string textb = "";
	cout << "Inserte el texto a traducir: ";
	getline(cin, text);
	for (char character : text) {
		textb += diccionario[character];
	}
	cout << text << " significa " << textb << " en lenguaje leet";
}
