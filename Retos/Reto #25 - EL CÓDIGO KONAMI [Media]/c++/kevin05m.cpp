#include <iostream>
#include <sstream>

using namespace std;

int validarCodigo(string konami, int i){
    const string codigoKonami[] = {"arriba", "arriba", "abajo", "abajo", "izquierda", "derecha", "izquierda", "derecha", "B", "A"};
    int cont = 0;
    if(konami == codigoKonami[i]){
        cont = cont + 1;
    }
    return cont;
}

int main(){
    string codKonami, konami[10];
    int cont=0, i=0;
    cout << "Ingrese el código Konami completo (EJ: arriba-izquierda-etc): ";
    cin >> codKonami;
    stringstream input_stringstream(codKonami);
    while(getline(input_stringstream, konami[i], '-')){
        cont = cont + validarCodigo(konami[i], i);
        i++;
    }
    if(cont == 10){
        cout << "Código Kunami correcto!";
    } else {
        cout << "Código Kunami incorrecto!";
    }
    return 0;
}

// input test: arriba-arriba-abajo-abajo-izquierda-derecha-izquierda-derecha-B-A