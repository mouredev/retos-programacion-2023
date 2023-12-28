/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<char> stringCheck(const string &str1, const string &str2);
void printVector(const vector<char> &vec);

int main(){

    string str1 = "Me llamo mouredev";
    string str2 = "Me llemo mouredov";

    vector<char> result = stringCheck(str1, str2);
    printVector(result);

    str1 = "Me llamo.Brais Moure";
    str2 = "Me llamo brais moure";
    result.clear();
    result = stringCheck(str1, str2);
    printVector(result);

    str1 = "Me llamo brais moure";
    str2 = "Me llamo brais";
    result.clear();
    result = stringCheck(str1, str2);
    printVector(result);

    return 0;
}

vector<char> stringCheck(const string &str1, const string &str2){

    vector<char> arr;

    if(str1.length() != str2.length()){
        cout << "Strings are not the same length" << endl;
        return arr;
    }

    for(unsigned int i = 0; i < str1.length(); i++){
        if(str1[i] != str2[i]){
            arr.push_back(str2[i]);
        }
    }
    return arr;
}

void printVector(const vector<char> &vec){

    cout << "[";
    for (unsigned int i = 0; i < vec.size(); ++i) {
        cout << " '" << vec[i] << "'";
        if (i < vec.size() - 1) {
            cout << ",";
        }
    }
    cout << " ]" << endl;
}