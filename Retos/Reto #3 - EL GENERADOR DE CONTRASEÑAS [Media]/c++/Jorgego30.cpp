/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

#include <bits/stdc++.h>
using namespace std;

int main(){
    srand(time(0));
    string a="abcdefghijklmnopqrstuvwxyz", A="ABCDEFGHIJKLMNOPQRSTUVWXYZ", n="1234567890", e="!\"$\\%&/()=?¿*^¨_:;,.-`+'@|";

    int l=0;
    string a_="", A_="", n_="", e_="";

    bool f=1;

    cout << "Introduce el numero de caracteres de la contrasenha: "; cin >> l;

    string c[l];

    while (f==1){
        if (l<8 || l>16){
            cout << "\nLa longitud de la contrasenha debe estar comprendida entre 8 y 16 caracteres" << endl;
            cout << "\nIntroduce de nuevo el numero de caracteres: "; cin >> l;
        }else {
            f=0;
            break;
        }
    }

    cout << "\nQuieres que la contrasenha tenga letras en minuscula? (y/n) "; cin >> a_;
    cout << "\nQuieres que la contrasenha tenga letras en mayuscula? (y/n) "; cin >> A_;
    cout << "\nQuieres que la contrasenha tenga numeros? (y/n) "; cin >> n_;
    cout << "\nQuieres que la contrasenha tenga caracteres especiales? (y/n) "; cin >> e_;
    cout << endl;

    string t="";

    if (a_=="y" && A_=="y" && n_=="y" && e_=="y"){
        t+=a;
        t+=A;
        t+=n;
        t+=e;
    }else if(a_=="y" && A_=="y" && n_=="y"){
        t+=a;
        t+=A;
        t+=n;
    }else if(a_=="y" && A_=="y" && e_=="y"){
        t+=a;
        t+=A;
        t+=e;
    }else if(a_=="y" && n_=="y" && e_=="y"){
        t+=a;
        t+=n;
        t+=e;
    }else if(A_=="y" && n_=="y" && e_=="y"){
        t+=A;
        t+=n;
        t+=e;
    }else if(a_=="y" && A_=="y"){
        t+=a;
        t+=A;
    }else if(a_=="y" && n_=="y"){
        t+=a;
        t+=n;
    }else if(a_=="y" && e_=="y"){
        t+=a;
        t+=e;
    }else if(A_=="y" && n_=="y"){
        t+=A;
        t+=n;
    }else if(A_=="y" && e_=="y"){
        t+=A;
        t+=e;
    }else if(n_=="y" && e_=="y"){
        t+=n;
        t+=e;
    }else if(a_=="y"){
        t+=a;
    }else if(A_=="y"){
        t+=A;
    }else if(n_=="y"){
        t+=n;
    }else if(e_=="y"){
        t+=e;
    }

    for (int i=0; i<l; i++){
        int numero_aleatorio=rand()%t.size();
        c[i]=t[numero_aleatorio];
    }

    cout << c;



}