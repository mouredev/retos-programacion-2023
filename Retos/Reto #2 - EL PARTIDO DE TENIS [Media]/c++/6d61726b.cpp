#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

int main()
{
	map<int, string> PUNTOS = {
		{0, "Love"},
    	{1, "15"},
    	{2, "30"},
    	{3, "40"}
	};

	string texto = "P1 P1 P2 P2 P1 P2 P1 P1";
	istringstream iss(texto);
	vector<string> listaJugadores;
    string palabra;

    while (getline(iss, palabra, ' ')) {
        listaJugadores.push_back(palabra);
    }

	int puntosJugador1 = 0;
	int puntosJugador2 = 0;

	for (auto jugador : listaJugadores)
	{	
		if (puntosJugador1 == 4)
		{
			cout << "Deuce" << "\nVentaja P1" << "\nHa ganado el P1\n";
			break;
		}
		else if (puntosJugador2 == 4)
		{
			cout << "Deuce" << "\nVentaja P2" << "\nHa ganado el P2\n";
			break;
		}

		if (jugador == "P1")
		{
			cout << PUNTOS[puntosJugador1] << " - " << PUNTOS[puntosJugador2];
			puntosJugador1++;
		}
		else if (jugador == "P2")
		{	
			cout << PUNTOS[puntosJugador1] << " - " << PUNTOS[puntosJugador2];
			puntosJugador2++;
		}

		cout << endl;
	}

	return 0;
}