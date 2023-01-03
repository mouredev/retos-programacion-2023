#include <iostream>
using namespace std;

int main(){

    int numero=1;

    while(numero<=100){

        if(numero%3==0){
            if (numero%5==0){
            cout<<"fizz Buzz"<<endl;
        }
            cout<<"fizz"<<endl;
        }
        else if (numero%5==0){
            cout<<"buzz"<<endl;
        }
        else{
            cout<<numero<<endl;
        }
    numero++;
    }
}
