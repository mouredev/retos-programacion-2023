#include<iostream>
#include<map>
#include<string>
using namespace std;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 
void transformText(string text);

map<char, string> dictionary = {
  {'a', "4"}, {'b', "I3"}, {'c', "["}, {'d', ")"}, {'e', "3"},
  {'f', "|="}, {'g', "&"}, {'h', "#"}, {'i', "1"}, {'j', ",_|"},
  {'k', ">|"}, {'l', "1"}, {'m', "/\\/\\"}, {'n', "^/"}, {'o', "0"},
  {'p', "|*"}, {'q', "(_,)"}, {'r', "I2"}, {'s', "5"}, {'t', "7"},
  {'u', "(_)"}, {'v', "\\/"}, {'w', "\\/\\/"}, {'x', "><"},
  {'y', "j"}, {'z', "2"}, {'1', "L"}, {'2', "R"}, {'3', "E"},
  {'4', "A"}, {'5', "S"}, {'6', "b"}, {'7', "T"}, {'8', "B"},
  {'9', "g"}, {'0', "o"}
};

int main(){
	transformText("Hello World");
	transformText("Aprendiendo Python con Mouredev");
	
	return 0;
}

void transformText(string text){
	string newText = "";
	
	for(int i=0; i<text.length(); i++){
		if (dictionary.find(text[i]) != dictionary.end()) {
			newText += dictionary[tolower(text[i])];
		} else {
			newText += text[i];
		}
	}

	cout << newText << endl;	
}
