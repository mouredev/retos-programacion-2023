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
#include <stdlib.h>
#include <string>

std::string PasswordGenerator(int Length, bool UpperCase, bool Numbers, bool Symbols);

int main() {
    std::string _Password = "";
    int _Length = 0;
    bool _UpperCase = 0;
    bool _Numbers = 0;
    bool _Symbols = 0;

    std::cout << "Longitud (8 - 16): ";
    std::cin >> _Length;
    std::cout << "Mayusculas? Si(1) - No(0): ";
    std::cin >> _UpperCase;
    std::cout << "Numeros? Si(1) - No(0): ";
    std::cin >> _Numbers;
    std::cout << "Simbolos? Si(1) - No(0): ";
    std::cin >> _Symbols;
    _Password = PasswordGenerator(_Length, _UpperCase, _Numbers, _Symbols);
    std::cout << "Password: " << _Password << std::endl;
    return 0;
}

std::string PasswordGenerator(int Length, bool UpperCase, bool Numbers, bool Symbols) {
    if (Length <= 8 || Length >= 16) {
        std::cout << "Longitud Incorrecta" << std::endl;
    }

    std::string Password = "";
    int iAscii;

    if (UpperCase && Numbers && Symbols) {
        for (int i = 0; i < Length; i++) {
            iAscii = 33 + rand() % (127 - 33);
            Password += char(iAscii);
        }
        return Password;
    }

    if (UpperCase && Numbers) {
        for (int i = 0; i < Length; i++) {
            iAscii = 48 + rand() % (123 - 48);
            while ((iAscii >= 58 && iAscii <= 64) || (iAscii >= 91 && iAscii <= 96)) {
                iAscii = 48 + rand() % (123 - 48);
            }
        }
        return Password;
    }

    if (Numbers && Symbols) {
        for (int i = 0; i < Length; i++) {
            iAscii = 33 + rand() % (127 - 33);
            while (iAscii >= 65 && iAscii <= 90) {
                iAscii = 33 + rand() % (127 - 33);
            }
            Password += char(iAscii);
        }
        return Password;
    }

    if (UpperCase && Symbols) {
        for (int i = 0; i < Length; i++) {
            iAscii = 33 + rand() % (127 - 33);
            while (iAscii >= 48 && iAscii <= 57) {
                iAscii = 33 + rand() % (127 - 33);
            }
            Password += char(iAscii);
        }
        return Password;
    }

    if (UpperCase) {
        for (int i = 0; i < Length; i++) {
            iAscii = 65 + rand() % (123 - 65);
            while (iAscii >= 91 && iAscii <= 96) {
                iAscii = 65 + rand() % (123 - 65);
            }
            Password += char(iAscii);
        }
        return Password;
    }

    if (Numbers) {
        for (int i = 0; i < Length; i++) {
            iAscii = 48 + rand() % (123 - 48);
            while (iAscii >= 58 && iAscii <= 96) {
                iAscii = 48 + rand() % (123 - 48);
            }
            Password += char(iAscii);
        }
        return Password;
    }

    if (Symbols) {
        for (int i = 0; i < Length; i++) {
            iAscii = 33 + rand() % (127 - 33);
            while ((iAscii >= 48 && iAscii <= 57) || (iAscii >= 65 && iAscii <= 90)) {
                iAscii = 33 + rand() % (127 - 33);
            }
            Password += char(iAscii);
        }
        return Password;
    }
}