#include <iostream>
#include <string>
#include <iomanip>
using std::string;
using std::cout;
using std::endl;
using std::setw;
using std::cin;

void drawLadder(int n);
void ladderpositiv(int n);
void ladderNegativ(int n);

int main() {
    int escalon;
    do {
        cout << "Ingrese el numero de escalones: ";
        cin >> escalon;

        if (cin.fail() || cin.eof()) {
            break;
        }

        drawLadder(escalon);
    } while (escalon);

    return 0;
}

void ladderNegativ(int n){
    n=n*-1;
    string parte1="_", parte2="|_";
    for(int i=1; i<=n; i++){
        if(i==1) {
            cout<<parte1<<endl;
        }

        for(int j=1; j<=i-1; j++){
            cout<<" ";
        }
        cout<<parte2<<endl;

    }
}


void ladderPositiv(int n){
    string parte1="_", parte2="_|";

    for(int i=n; i>=1; i--){
        if(i==n) {
            for(int j=1; j<=i; j++){
                cout<<" ";
            }
            cout<<parte1<<endl;
        }


        for(int j=1; j<=i-1; j++){
            cout<<" ";
        }
        cout<<parte2<<endl;

    }
}


void drawLadder(int n){
    if(n>0) {
        ladderPositiv(n);
    }else if(n<0){
        ladderNegativ(n);
    }else{
        cout<<"__"<<endl;
    }
}









