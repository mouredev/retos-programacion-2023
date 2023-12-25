#include <iostream>
#include <string>
#include <map>
#include <cmath>

using namespace std;

const int P1 = 0;
const int P2 = 1;

const int positions[8] = { P1, P1, P2, P2, P1, P2, P1, P1 };
const string textT[5] = { "Love","15","30","40","juego" };

int dif;
int estado_Player[2] = { 0,0 };
string texts[2] = {};

int static getDiferencia() {
	return abs(estado_Player[0] - estado_Player[1]);
}
bool static isFinish() {
	if ((estado_Player[0] >= 5 or estado_Player[1] >= 5) and (getDiferencia() > 1)) {
		return false;
	}
	return true;

}
void main()
{
	int i = 0;
	do {

		estado_Player[positions[i]]++;
		i++;

		if (estado_Player[0] >= 3 and estado_Player[1] >= 3) {
			if (estado_Player[0] == 3 and estado_Player[1] == 3) {
				cout << "Deuce" << endl;
			}
			else {
				dif = getDiferencia();
				if (estado_Player[0] > estado_Player[1]) {
					if (dif > 1) {
						cout << "Ha ganado el P1";
					}
					else {
						cout << "Ventaja P1" << endl;
					}
				}
				else {
					if (dif > 1) {
						cout << "Ha ganado el P2";
					}
					else {
						cout << "Ventaja P2" << endl;
					}
				}
			}
		}
		else {
			for (int key = 0; key <= 1; key++) {
				texts[key] = textT[estado_Player[key]];
			}
			cout << texts[0] << " - " << texts[1] << endl;
		}
	} while (isFinish());
	

}
