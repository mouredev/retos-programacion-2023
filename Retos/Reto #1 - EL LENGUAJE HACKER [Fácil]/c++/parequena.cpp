/*
 *              Reto #1: EL "LENGUAJE HACKER"
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

#include <unordered_map>
#include <string>
#include <iostream>
#include <string_view>

static std::unordered_map<char, std::string> leet =
{
    {'a', "4"},      {'A', "4"},
    {'b', "|3"},     {'B', "|3"},
    {'c', "["},      {'C', "["},
    {'d', ")"},      {'D', ")"},
    {'e', "3"},      {'E', "3"},
    {'f', "|="},     {'F', "|="},
    {'g', "&"},      {'G', "&"},
    {'h', "#"},      {'H', "#"},
    {'i', "1"},      {'I', "1"},
    {'j', ",_|"},    {'J', ",_|"},
    {'k', ">|"},     {'K', ">|"},
    {'l', "1"},      {'L', "1"},
    {'m', "/\\/\\"}, {'M', "/\\/\\"},
    {'n', "^/"},     {'N', "^/"},
    {'o', "0"},      {'O', "0"},
    {'p', "|*"},     {'P', "|*"},
    {'q', "(_,)"},   {'Q', "(_,)"},
    {'r', "I2"},     {'R', "I2"},
    {'s', "5"},      {'S', "5"},
    {'t', "7"},      {'T', "7"},
    {'u', "(_)"},    {'U', "(_)"},
    {'v', "\\/"},    {'V', "\\/"},
    {'w', "\\/\\/"}, {'W', "\\/\\/"},
    {'x', "><"},     {'X', "><"},
    {'y', "j"},      {'Y', "j"},
    {'z', "2"},      {'Z', "2"},
    {'1', "L"}, {'2', "L"}, {'3', "E"}, {'4', "A"}, {'5', "S"}, {'6', "b"}, {'7', "T"}, {'8', "B"}, {'9', "g"}, {'0', "o"}, 
};

void printL33tText(std::string_view const str)
{
    std::string out{};
    for(auto const s : str)
    {
        std::string l = leet[s];
        if(l.empty()) // Update with unkown characters.
        {
            l = s;
            leet[s] = s;
        };
        out += l;
    }

    std::cout << out << '\n';
}

int main()
{
    printL33tText("Hola, me llamo Pablo.");
    return 0;
}