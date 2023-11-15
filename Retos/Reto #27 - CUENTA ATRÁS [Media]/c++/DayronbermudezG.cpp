/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

#include <iostream>
#include <windows.h>

void cuentaAtras(int inicio, int segundos) {
    
    for(int i = inicio; i >= 0; i--) {

        std::cout << i << std::endl;
        
        if (i == 0) break;
        Sleep(segundos*1000);
    }
}

int main(){

    int inicio_cuenta;
    int segundos;

    do {

        std::cout << "Represente el número en el que comienza la cuenta: "; std::cin >> inicio_cuenta;
        std::cout << "Ingrese los segundos que tienen que transcurrir entre cada cuenta: "; std::cin >> segundos;
        std::cout << std::endl;

        cuentaAtras(inicio_cuenta, segundos);
        std::cout << std::endl;

    }while(true);

    return 0;
}
