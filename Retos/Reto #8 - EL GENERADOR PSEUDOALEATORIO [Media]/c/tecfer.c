// Reto #8: El generador pseudoaleatorio
// Crea un generador de números pseudoaleatorios entre 0 y 100.
// -No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#include <stdio.h>
#include <time.h>

int pseudoaleatorio(void); 

int main()
{
    printf("%i",pseudoaleatorio());
    return 0;
}


int pseudoaleatorio()
{
    int numero = time(NULL);
    numero = numero*25184;
    return numero%101;
}


