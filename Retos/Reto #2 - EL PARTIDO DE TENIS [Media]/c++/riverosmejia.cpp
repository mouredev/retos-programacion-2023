#include <iostream>
#include <string>

using namespace std;

int main() {
    int player1Score = 0,player2Score = 0;
    bool deuce = false;
    bool advantage = false;

    string input;

    while (true) {
        cout << "Ingresa el jugador que gana el punto (P1 o P2): ";
        cin >> input;

        if (input == "P1") {
            player1Score++;
        } else if (input == "P2") {
            player2Score++;
        }

        cout << "Puntuación actual: " << player1Score << " - " << player2Score << endl;

        if (player1Score >= 2 && player2Score >= 2) {
            if (player1Score == player2Score) {
                deuce = true;
                cout << "Deuce" << endl;
            } else if (player1Score > player2Score) {
                deuce = false;
                advantage = true;
                cout << "Ventaja P1" << endl;
            } else {
                deuce = false;
                advantage = true;
                cout << "Ventaja P2" << endl;
            }
        }

        if (player1Score >= 4 && player1Score - player2Score >= 2) {
            cout << "Ha ganado el P1" << endl;
            break;
        } else if (player2Score >= 4 && player2Score - player1Score >= 2) {
            cout << "Ha ganado el P2" << endl;
            break;
        }
    }

    return 0;
}
