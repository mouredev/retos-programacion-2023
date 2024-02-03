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
using namespace std;
int main() {
    string texto;
    getline(cin, texto);
    for (char c : texto) {
        switch (c) {
            case 'a':
                cout << "4";
                break;
            case 'e':
                cout << "3";
                break;
            case 'i':
                cout << "1";
                break;
            case 'o':
                cout << "0";
                break;
            case 's':
                cout << "5";
                break;
            case 't':
                cout << "7";
                break;
            default:
                cout << c;
                break;
        }
    }
    return 0;
}