#include <iostream>
#include <cstdlib>

using namespace std;

int main(){

    for(int cont=1;cont<=100;cont++){

        if(cont%3==0&&cont%5==0){

            cout<<cont<<"-fizzbuzz\n";

        }

        else if(cont%3==0){

            cout<<cont<<"-fizz\n";

        }

        else if(cont%5==0){

            cout<<cont<<"-buzz\n";

        }

    }

    cin.get(); //comando para pausar pantalla, solo dar enter y el programa termina

    return 0;

}