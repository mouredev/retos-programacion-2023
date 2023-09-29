#include <iostream>
using namespace std;

bool es_fibonacci(int n){
    int a = 0, b = 1;

    while (b < n)
    {
        int varTemp = a;
        a = b;
        b = varTemp + b; 
    }

    return b == n;
}

bool es_par(int n){
    return n % 2 == 0;
}

bool es_primo(int n){
    if (n < 2){
        return false;
    }
    for (int i = 2; i < n; i++){
        if (n % i == 0){
            return false;
        }
    }
    return true;
}


int main(){

    int num;
    cout << "Ingrese un numero: ";
    cin >> num;

    string res_final = "";

    if (es_primo(num)){
        res_final += "es primo, ";
    }else{
        res_final += "no es primo, ";
    }

    if (es_fibonacci(num)){
        res_final += "fibonacci, ";
    }else{
        res_final += "no es fibonacci, ";
    }

    if (es_par(num)){
        res_final += "y es par.";
    }else{
        res_final += "y es impar.";
    }

    cout << res_final;

}
