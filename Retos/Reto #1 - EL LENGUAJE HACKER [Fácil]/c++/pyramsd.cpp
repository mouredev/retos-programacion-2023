#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(){
    map<char, string> dicctionary = {
        {'a', "4"}, {'b', "I3"}, {'c', "["}, {'d', ")"}, {'e', "3"}, {'f', "|="}, {'g', "&"}, 
        {'h', "#"}, {'i', "1"}, {'j', ",_|"}, {'k', ">|"}, {'l', "1"}, {'m', "/\\/\\"},
        {'n', "^/"}, {'o', "0"}, {'p', "|*"}, {'q', "(_,)"}, {'r', "|2"}, {'s', "5"}, {'t', "7"},
        {'u', "(_)"}, {'v', "\\/"}, {'w', "\\/\\/"}, {'x', "><"}, {'y', "j"}, {'z', "2"},
        {'1', "L"}, {'2', "R"}, {'3', "E"}, {'4', "A"}, {'5', "S"}, {'6', "b"}, {'7', "T"},
        {'8', "B"}, {'9', "g"}, {'0', "o"}
    };

    string texto;
    cout << "Ingrese texto: ";
    getline(cin, texto);

    string textoTraducido = "";

    for (char i : texto){
        char lowerCase = tolower(i);
        if (dicctionary.count(lowerCase) > 0){
            textoTraducido += dicctionary[lowerCase];
        }else{
            textoTraducido += i;
        }
    }

    cout << textoTraducido;

}