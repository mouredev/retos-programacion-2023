#include <iostream>
using namespace std;

int main(){

    cout<<"frase:";
    string frase,tH="";
    frase="fabio zerpa tiene razon, hay marcianos entre la gente";
    cout<<frase<<"\n\n";

    for (int i=0; i<=frase.size(); i++){
        switch(frase[i]){
            case 'a': tH.push_back('4'); break;
            case 'b': tH.push_back('I'),tH.push_back('3'); break;
            case 'c': tH.push_back('['); break;
            case 'd': tH.push_back(')'); break;
            case 'e': tH.push_back('3'); break;
            case 'f': tH.push_back('|'),tH.push_back('='); break;
            case 'g': tH.push_back('&'); break;
            case 'h': tH.push_back('#'); break;
            case 'i': tH.push_back('1'); break;
            case 'j': tH.push_back(','), tH.push_back('_'),tH.push_back('|'); break;
            case 'k': tH.push_back('>'),tH.push_back('|'); break;
            case 'l': tH.push_back('1'); break;
            case 'm': tH.push_back('/'),tH.push_back('\\'); break; 
            case 'n': tH.push_back('^'),tH.push_back('/'); break;
            case 'o': tH.push_back('0'); break;
            case 'p': tH.push_back('|'),tH.push_back('*'); break;
            case 'q': tH.push_back('('),tH.push_back('_'),tH.push_back(','),tH.push_back(')'); break;
            case 'r': tH.push_back('I'),tH.push_back('2'); break;
            case 's': tH.push_back('5'); break;
            case 't': tH.push_back('7'); break;
            case 'u': tH.push_back('('),tH.push_back('_'),tH.push_back(')'); break;
            case 'v': tH.push_back('\\'),tH.push_back('/'); break;
            case 'w': tH.push_back('\\'),tH.push_back('/'),tH.push_back('\\'),tH.push_back('/'); break;
            case 'x': tH.push_back('>'),tH.push_back('<'); break;
            case 'y': tH.push_back('j'); break;
            case 'z': tH.push_back('2'); break;
            case '1': tH.push_back('L'); break;
            case '2': tH.push_back('R'); break;
            case '3': tH.push_back('E'); break;
            case '4': tH.push_back('A'); break;
            case '5': tH.push_back('S'); break;
            case '6': tH.push_back('b'); break;
            case '7': tH.push_back('T'); break;
            case '8': tH.push_back('B'); break;
            case '9': tH.push_back('g'); break;
            case '0': tH.push_back('o'); break;
            case ' ': tH.push_back(' '); break;
        }
    }

    cout <<"frase traducida: "<< tH << "\n\n";

}