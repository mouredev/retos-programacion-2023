#include <iostream>
#include <map>
#include <string>
using namespace std;

string lenguaje_hacker(char caracter){
    map<string, string> leet_alphabet = {
        {"a", "4",},
        {"b", "I3",},
        {"c", "[",},
        {"d", ")",},
        {"e", "3",},
        {"f", "|=",},
        {"g", "&",},
        {"h", "#",},
        {"i", "1",},
        {"j", ",_|",},
        {"k", ">|",},
        {"l", "1",},
        {"m", "/\\/\\",},
        {"n", "^/",},
        {"o", "0",},
        {"p", "|*",},
        {"q", "(_,)",},
        {"r", "I2",},
        {"s", "5",},
        {"t", "7",},
        {"u", "(_)",},
        {"v", "\\/",},
        {"w", "\\/\\/",},
        {"x", "><",},
        {"y", "j",},
        {"z", "2",},
        {"1", "L",},
        {"2", "R",},
        {"3", "E",},
        {"4", "A",},
        {"5", "S",},
        {"6", "b",},
        {"7", "T",},
        {"8", "B",},
        {"9", "g",}
    };

    // Comprobamos que el caracter pasado como argumento es traducible con nuestro diccionario.
    bool exists;
    string cadena;
    cadena.push_back(caracter);
    if (leet_alphabet.find(cadena) == leet_alphabet.end()){
        exists = false;
    } else {
        exists = true;
    }

    // Si se puede traducir retornamos el valor traducido.
    // Sino, retornamos el caracter que hemos pasado a la función.
    if (exists == true){
        return leet_alphabet[cadena];
    } else {
        return cadena;
    }
}

int main(){
    string text, new_text;
    cout<<"Introduce el texto que desea traducir: "<<endl; getline(cin, text);

    // Convertimos todo el texto a minúsculas y traducimos.
    for (int i=0; i < text.length(); i++){
        text[i] = tolower(text[i]);
        new_text = new_text + lenguaje_hacker(text[i]);
    }

    // Imprimimos por pantalla.
    cout<<"El texto traducido es: "<<endl;
    cout<<new_text<<endl;

    return 0;
}

