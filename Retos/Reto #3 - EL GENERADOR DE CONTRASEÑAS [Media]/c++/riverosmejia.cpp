#include <iostream>
#include <ctime>
#include <random>

using namespace std;

//-----//

const string base="abcdefghijklmnopqrstuvwxyz";
const string mayus="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string nums="1234567890";
const string carc="()/%$#,;.:+-*|°'?¿¡[]{}¨´";

//-----//

void generar(char opciones[3]);


int main(){

    char confirm[3];

    cout<<"incluir mayuscuas? (s/n):";
    cin>>confirm[0];

    cout<<"\nincluir numeros? (s/n):";
    cin>>confirm[1];

    cout<<"\nincluir caracteres? (s/n):";
    cin>>confirm[2];

    generar(confirm);

    cin.get(); //forma de apusar el programa, solo dar enter y el programa terminará
    return 0;

}

void generar(char opciones[3]){

    string caracteres=base;

    if(opciones[0]=='s'){caracteres+=mayus;}

    if(opciones[1]=='s'){caracteres+=nums;}

    if(opciones[2]=='s'){caracteres+=carc;}

    mt19937 gen1(static_cast<unsigned>(time(0)));  // Generador de números aleatorios
    uniform_int_distribution<int> distribucion1(8,16);

    int longitud=distribucion1(gen1);

    mt19937 gen(static_cast<unsigned>(time(0)));  // Generador de números aleatorios
    uniform_int_distribution<int> distribucion(0, caracteres.length() - 1);

    string contrasena;

    for (int i = 0; i < longitud; i++) {
        int indice = distribucion(gen);
        contrasena += caracteres[indice];
    }

    cout<<"\n"<<contrasena;

}

