/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
#include <iostream>
#include <map>

using namespace std;

map<string,string> leet_alphabet = {
    {"A","4"},
    {"B","I3"},
    {"C","[]"},
    {"D",")"},
    {"E","3"},
    {"F","|="},
    {"G","&"},
    {"H","#"},
    {"I","1"},
    {"J",",_|"},
    {"K",">|"},
    {"L","1"},
    {"M","/\\/\\"},
    {"N","^/"},
    {"O","0"},
    {"P","|*"},
    {"Q","(_,)"},
    {"R","I2"},
    {"S","5"},
    {"T","7"},
    {"U","(_)"},
    {"V","\\/"},
    {"W","\\/\\/"},
    {"X","><"},
    {"Y","j"},
    {"Z","2"},
    {"1","L"},
    {"2","R"},
    {"3","E"},
    {"4","A"},
    {"5","S"},
    {"6","b"},
    {"7","T"},
    {"8","B"},
    {"9","g"},
    {"0","o"}
};

string convertToHackerCode(string text){

    string convertedText = "";

    for (int i = 0; i < text.length(); i++) {
        string character;
        character.push_back(toupper(text[i]));
        
        if (leet_alphabet.count(character)){
            convertedText += leet_alphabet[character];
        }
        else{
            convertedText += text[i];
        }
    }
    return convertedText;
}

int main(){   

    string result = convertToHackerCode("Hello World!");

    cout << result << endl;

    result = convertToHackerCode("mouredev");

    cout << result << endl;
}