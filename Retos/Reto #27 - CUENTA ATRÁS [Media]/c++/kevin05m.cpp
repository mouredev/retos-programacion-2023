#include <iostream>
#include <unistd.h>

using namespace std;

void cuentaAtras(int start, int second){
    for (int i = start; i >= 0; i--){
        cout << i << endl;
        if(i == 0){
            return;
        }
        usleep(second);
    }
    
}

int main(){
    int start, second;
    cin >> start >> second;
    second = second * 1e6;
    cuentaAtras(start, second);
    return 0;
}