#include <iostream>

//A cambio de 44 bytes de RAM obtenemos:
//  -Un mejor uso de la caché de datos, al extraer las cadenas de texto de lamisma zona de 44 bytes 
//  -Un mejor uso de la caché de instrucciones, ya que eliminamos los condicionales
//Por lo tanto, es esperable que la ejecución sea más rápida que con los cláscios if/else
const char textos[4][11] = {          
    "\n\0",                        
    "\rfizz\n\0",                   
    "\rbuzz\n\0",       
    "\rfizzbuzz\n"
};

int main(int argc, char *argv[]){

    for (int i = 1; i <= 100; ++i){
        uint16_t result = i | ((i%3==0)<<8) | ((i%5==0)<<9);
        std::cout << (result & 255) << textos[result>>8];
    }
}