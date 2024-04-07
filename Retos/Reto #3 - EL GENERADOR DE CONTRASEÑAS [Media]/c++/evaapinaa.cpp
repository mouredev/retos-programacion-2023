/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

#include <iostream>
#include <string>
#include <time.h>

using namespace std;

void genPassword(int longitud) {

    string contrasena;
    string caracteres = "abcdefghijklmnopqrstuvwxyz";
    bool incluirMayus,incluirNum,incluirSimb;

    cout << "Desea incluir letras mayusculas? (0/1): ";
    cin >> incluirMayus;

    cout << "Desea incluir numeros? (0/1): ";
    cin >> incluirNum;

    cout << "Desea incluir simbolos? (0/1): ";
    cin >> incluirSimb;

    if (incluirMayus) caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (incluirNum) caracteres += "0123456789";
    if (incluirSimb) caracteres += "!@#$%^&*()_+=-[]{}|;:,.<>?";
    
    cout << "\nGenerando contasena..." << endl;

    for(int i=0;i<longitud;i++) {
        char letra = rand() % caracteres.length(); 
        contrasena += caracteres[letra];
    }

    cout << "Se ha generado -> " << contrasena << endl;

}

int main(){

    srand(time(NULL));
    
    int longitud;

    cout << "Introduzca la longitud (entre 8-16): ";
    cin >> longitud;

    genPassword(longitud);

    return 0;
}