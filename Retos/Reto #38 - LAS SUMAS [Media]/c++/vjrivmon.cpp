#include <iostream>
#include <vector>
using namespace std;

void buscarCombinaciones(vector<int>& lista, int objetivo, vector<int>& combinacion, int suma, int inicio) {
    if (suma == objetivo) {
        for (int num : combinacion) {
            cout << num << " ";
        }
        cout << endl;
        return;
    }

    for (int i = inicio; i < lista.size(); i++) {
        if (suma + lista[i] <= objetivo) {
            combinacion.push_back(lista[i]);
            buscarCombinaciones(lista, objetivo, combinacion, suma + lista[i], i + 1);
            combinacion.pop_back();
        }
    }
}

void valorObjetivo(vector<int>& lista, int objetivo) {
    vector<int> combinacion;
    buscarCombinaciones(lista, objetivo, combinacion, 0, 0);
}

int main() {
    vector<int> lista = {1, 5, 3, 2};
    int objetivo = 6;

    cout << "Combinaciones que suman " << objetivo << ": " << endl;
    valorObjetivo(lista, objetivo);

    return 0;
}