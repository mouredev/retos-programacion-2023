#include <iostream>
#include <map>
#include <string>
using namespace std;

string TennisGame(string points[], int length){

    cout<<"PARTIDO DE TENIS:"<<endl;
    cout<<"P1 - P2"<<endl<<endl;

    // Variables
    int counter_P1 = 0, counter_P2 = 0;
    string winner = "";
    map<int, string> PointsSystem = {
        {0, "Love"},
        {1, "15"},
        {2, "30"},
        {3, "40"}
    };

    for (int i=0; i<length; i++){
        // Control de errores en la entrada
        if ((points[i] != "P1") && (points[i] != "P2")){
            return "No se ha introducido correctamente la secuencia de puntos.";
        }

        if (points[i] == "P1"){
            counter_P1++;
        } else {
            counter_P2++;
        }

        // Impresión de los resultados.
        if ((counter_P1 <= 3 && counter_P2 < 3) || (counter_P1 < 3 && counter_P2 <= 3)){
            cout<<PointsSystem[counter_P1] << " - " << PointsSystem[counter_P2]<<endl;
        } else if (counter_P1 == counter_P2){
            cout<<"Deuce"<<endl;
        } else if (counter_P1 - counter_P2 == 1){
            cout<<"Ventaja P1"<<endl;
        } else if (counter_P2 - counter_P1 == 1)
            cout<<"Ventaja P2"<<endl;
        else{
            if (counter_P2>counter_P1){
                winner = "El ganador es P2";
            } else {
                winner = "El ganador es P1";
            }
        }
    }

    if (winner == ""){
        return "La longitud de los puntos introducidos no da como resultado un ganador.";
    } else{
        return winner;
    }
}

int main(){
    // Para añadir o quitar puntos a la lista habría que cambiar también el valor de length
    int length = 10;
    string points[length] = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P1", "P1"};
    cout<<TennisGame(points, length)<<endl;

    return 0;
}