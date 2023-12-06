#include <string>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string cifrar(string msj, int llave) {

    transform(msj.begin(), msj.end(), msj.begin(), ::toupper);
    
    string msj_cifrado;

    for (int i = 0; i < msj.size(); i++) {
        if (msj.at(i) > 'Z' or msj.at(i) < 'A') {
            msj_cifrado += msj.at(i);
            continue;
        }
        msj_cifrado += (msj.at(i) + llave) > 'Z' ? 'A' + ((msj.at(i) + llave) % ('Z' + 1)) : (msj.at(i) + llave);
    }

    return msj_cifrado;
}

string descifrar(string msj, int llave) {

    transform(msj.begin(), msj.end(), msj.begin(), ::toupper);

    string msj_descifrado;

    for (int i = 0; i < msj.size(); i++) {
        if (msj.at(i) > 'Z' or msj.at(i) < 'A') {
            msj_descifrado += msj.at(i);
            continue;
        }
        msj_descifrado += (msj.at(i) - llave) > 'Z' ? 'A' + ((msj.at(i) - llave) % ('Z' + 1)) : (msj.at(i) - llave);
    }

    return msj_descifrado;;
}

int main() {

    string msj = "Hola, Mundo!";
    int llave = 3;

    for (char c = 'A'; c <= 'Z'; c++) {
        cout << c << "|";
    }
    cout << "\n";
    
    for (char c = 'A'; c <= 'Z'; c++) {
        cout << static_cast<char>(c + llave > 'Z' ? 'A' + ((c + llave) % ('Z' + 1)) : (c + llave))  << "|";
    }
    cout << "\n";

    cout << "Mensaje Cifrado   : " << (msj = cifrar(msj, llave)) << endl;
    cout << "Mensaje Descifrado: " << descifrar(msj, llave) << endl;

    /* SALIDA
    A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
    D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|A|B|C|
    Mensaje Cifrado   : KROD, PXQGR!
    Mensaje Descifrado: HOLA, MUNDO!
    */
        
    return 0;
}
