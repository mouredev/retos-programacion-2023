#include <iostream>
#include <string>
#include <random>
using namespace std;


string generatePassword(int tam){
    string characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>/?";
    string paswd;

    // se encarga de obtener una semilla aleatoria
    random_device rd;
    // utiliza esa semilla para generar la secuencia de números aleatorios
    mt19937 generator(rd());

    // Establece un rango de numeros
    uniform_int_distribution<int> distribution(0, characters.length() -1);

    for (int i = 0; i < tam; i++){
        int randomIndex = distribution(generator);
        paswd += characters[randomIndex];
    }

    return paswd;
}


int main(){
    random_device rd;
    mt19937 generator(rd());

    int min = 8, max = 16;

    uniform_int_distribution<int> tamDitribution(min, max);
    // 'generator' sigue la regla de tamDitribution que es un numero entre 'min' y 'max'
    int tamPaswd = tamDitribution(generator);

    string paswd = generatePassword(tamPaswd);

    cout << paswd;
}
