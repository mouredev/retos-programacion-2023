/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

#include <iostream>
#include <string>
using namespace std;

string isPrime(int number){
    
    // Caso 0
    if (number == 0){
        return "El número no es primo";
    }

    // Caso positivo
    if (number > 0){
        for (int i=2; i<number; i++){
            if (number % i == 0){
                return "El número no es primo";
            }
        } return "El número es primo";
    }

    // Caso negativo
    if (number < 0){
        for (int i=-2; i>number; i--){
            if (number % i == 0){
                return "El número no es primo";
            }
        } return "El número es primo";
    }
}

string isEven(int number){
    if (number % 2 == 0){
        return "El número es par";
    } else{
        return "El número es impar";
    }
}

string isFibonacci(int number){

    // Controlamos números negativos
    if (number < 0){
        return "El número no es fibonacci";
    } else if (number == 0 || number == 1){
        return "El número es fibonacci";
    } else {
        int previous = 1, twoPrevious = 0, current;
        while(previous < number){
            current = previous + twoPrevious;
            twoPrevious = previous;
            previous = current;
            if (current == number){
                return "El número es fibonacci";
            }
        } return "El número no es fibonacci";
    }
}

int main(){
    int number;
    cout<<"Ingrese un número para realizar las comprobaciones: "<<endl; cin>>number;
    cout<<"--> "<<isPrime(number)<<endl;
    cout<<"--> "<<isFibonacci(number)<<endl;
    cout<<"--> "<<isEven(number)<<endl;

    return 0;
}