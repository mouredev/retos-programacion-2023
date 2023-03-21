/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

#include <bits/stdc++.h>
using namespace std;
 
 int main(){
    int num = 0;
    int x1 = 0;
    int x2 = 1;
    int x3 = 1;

    vector <int> fibonacci(100);

    for (int i=0; i<fibonacci.size(); i++){
        fibonacci[i]=x1 + x2;
        x3=x1 + x2;
        x1 = x2;
        x2 = x3;
    }

    cin >> num;

    bool primo=0;
    int par=0;

    if(num <= 1) { // 0 y 1 no son primos
        primo=false;
    }
    for(int i = 2; i <= num/2; i++) {
        if(num % i == 0) {
            primo=false;
        }else{
            primo=true;
        }
    }

    if (num%2==0){
        par=1;
    }

    if (primo==1 && par==1 && (count(fibonacci.begin(),fibonacci.end(),num)==1)){
        cout << "Este numero es primo, fibonacci y par" << endl;
    }else if (primo==0 && par==1 && (count(fibonacci.begin(),fibonacci.end(),num))==1){
        cout << "Este numero no es primo, es fibonnaci y par" << endl;
    }else if (primo==1 && par==0 && (count(fibonacci.begin(),fibonacci.end(),num))==1){
        cout << "Este numero es primo, fibonacci y es impar" << endl;
    }else if (primo==1 && par==1 && (count(fibonacci.begin(),fibonacci.end(),num))==0){
        cout << "Este numero es primo ni fibonacci, es par" << endl;
    }else if (primo==0 && par==1 && (count(fibonacci.begin(),fibonacci.end(),num))==0){
        cout << "Este numero no es primo ni fibonacci, es par" << endl;
    }else if (primo==0 && par==0 && (count(fibonacci.begin(),fibonacci.end(),num))==1){
        cout << "Este numero no es primo, es fibonacci y es impar" << endl;
    }else if (primo==1 && par==0 && (count(fibonacci.begin(),fibonacci.end(),num))==0){
        cout << "Este numero es primo, no es fibonacci y es impar" << endl;
    }else if (primo==0 && par==0 && (count(fibonacci.begin(),fibonacci.end(),num))==0){
        cout << "Este numero no es primo, no es fibonacci y es impar" << endl;
    }


 }
