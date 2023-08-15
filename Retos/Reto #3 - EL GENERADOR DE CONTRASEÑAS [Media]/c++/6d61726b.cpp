#include <iostream>
#include <string>
#include <random>

std::string generarContrasenia(int longitud = 8, bool mayusculas = false, bool numeros = false, bool simbolos = false);

int main()
{
	std::cout << generarContrasenia(32, true, true, true) << std::endl;
	return 0;
}

std::string generarContrasenia(int longitud, bool mayusculas, bool numeros, bool simbolos) {
    std::random_device rd;
    std::mt19937 gen(rd());

    std::string caracteresPermitidos = "abcdefghijklmnopqrstuvwxyz";

    if (longitud < 8)
        longitud = 8;
    else if (longitud > 16)
        longitud = 16;

    if (mayusculas)
        caracteresPermitidos += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    if (numeros)
        caracteresPermitidos += "0123456789";

    if (simbolos)
        caracteresPermitidos += "!\"#$%&'()*+,-./";

    std::uniform_int_distribution<int> dis(0, caracteresPermitidos.length() - 1);

    std::string contrasenia;
    for (int i = 0; i < longitud; i++)
        contrasenia += caracteresPermitidos[dis(gen)];

    return contrasenia;
}