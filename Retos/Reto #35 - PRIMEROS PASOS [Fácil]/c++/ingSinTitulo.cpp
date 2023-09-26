#include <iostream>
#include <vector>
#include <tuple>
#include <set>
#include <map>

using namespace std;

int main() {
    // Punto 1: Hola, mundo!
    cout << "Hola, mundo!" << endl;

    // Punto 2: Crea una variable de texto o string
    string miTexto = "¡Hola desde C++!";

    // Punto 3: Crea una variable de número entero
    int miEntero = 42;

    // Punto 4: Crea una variable de número con decimales
    double miDecimal = 3.14;

    // Punto 5: Crea una variable de tipo booleano
    bool miBooleano = true;

    // Punto 6: Crea una constante
    const int MI_CONSTANTE = 10;

    // Punto 7: Usa un if, else if y else
    if (miEntero > 50) {
        cout << "El número es mayor que 50" << endl;
    } else if (miEntero < 50) {
        cout << "El número es menor que 50" << endl;
    } else {
        cout << "El número es igual a 50" << endl;
    }

    // Punto 8: Crea un Array (vector en C++)
    vector<int> miVector = {1, 2, 3, 4, 5};

    // Punto 9: Crea una lista (vector en C++)
    vector<string> miLista = {"Manzana", "Banana", "Naranja"};

    // Punto 10: Crea una tupla
    tuple<int, string> miTupla = make_tuple(1, "Tupla");

    // Punto 11: Crea un set
    set<string> miSet = {"Rojo", "Verde", "Azul"};

    // Punto 12: Crea un diccionario (map en C++)
    map<string, string> miMapa = {
        {"clave1", "valor1"},
        {"clave2", "valor2"}
    };

    // Punto 13: Usa un ciclo for
    for (int i = 0; i < miVector.size(); i++) {
        cout << miVector[i] << endl;
    }

    // Punto 14: Usa un ciclo foreach
    for (const auto& elemento : miLista) {
        cout << elemento << endl;
    }

    // Punto 15: Usa un ciclo while
    int contador = 0;
    while (contador < 3) {
        cout << "Contador: " << contador << endl;
        contador++;
    }

    // Punto 16: Crea una función sin parámetros que no retorne nada
    void funcionSinParametros() {
        cout << "Función sin parámetros" << endl;
    }

    // Punto 17: Crea una función con parámetros que no retorne nada
    void funcionConParametros(int param1, const string& param2) {
        cout << "Parámetro 1: " << param1 << endl;
        cout << "Parámetro 2: " << param2 << endl;
    }

    // Punto 18: Crea una función con parámetros que retorne valor
    int funcionConRetorno(int a, int b) {
        return a + b;
    }

    // Punto 19: Crea una clase
    class Persona {
    public:
        string nombre;
        int edad;

        Persona(const string& nombre, int edad) : nombre(nombre), edad(edad) {}
    };

    // Punto 20: Muestra control de excepciones
    try {
        int resultado = miEntero / 0;
    } catch (const exception& e) {
        cout << "Error: " << e.what() << endl;
    }

    return 0;
}
