#include <iostream>
#include <cmath>

bool esCuadradoPerfecto(int numero);

int main()
{
	int numero;
	std::cin >> numero;

	std::string resultado = "";

	if (numero > 1)
	{
		if (numero == 2)
		{
			resultado += "es primo, ";
		}
		else
		{
			for (int i = 2; i < numero; i++)
			{
				if (numero % i == 0)
				{
					resultado += "no es primo, ";
					break;
				}
			}
			resultado += "es primo, ";
		}
	}
	else
		resultado += "no es primo, ";

	if (numero > 0 && (esCuadradoPerfecto(5 * numero * numero + 4) || esCuadradoPerfecto(5 * numero * numero - 4)))
		resultado += "es fibonacci ";
	else
		resultado += "no es fibonacci ";

	if (numero % 2 == 0)
		resultado += "y es par";
	else
		resultado += "y es impar";

	std::cout << numero << " " << resultado << std::endl;

	return 0;
}

bool esCuadradoPerfecto(int numero)
{
    auto resultado = std::sqrt(numero);
    return (resultado * resultado == numero);
}