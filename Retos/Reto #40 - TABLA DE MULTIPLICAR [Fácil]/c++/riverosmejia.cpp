
//se que se pudo hacer en un bucle normal pero me dio por repasar las funciones recursivas :,D

#include <iostream>

using namespace std;

void tabla(int num, int sob=1);

int main(){

    cout<<"dame un numero:";

    int num;

    cin>>num;

    tabla(num,1);

    return 0;

}

void tabla(int num, int sob){

    if(sob<11){

        int operacion=num*sob;+1;

        cout<<num<<" x "<<(sob)<<" = "<<operacion<<"\n";

        tabla(num,sob+1);

    }

}