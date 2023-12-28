#include <iostream>
#include <string>
#include <cstdlib>
#include <time.h>
using namespace std;

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

string PasswordGenerator(int length, bool upercase, bool numbers, bool symbols){

    // Control de errores en la longitud de la contraseña
    if (length<8 || length>12){
        return "Error en la longitud de la contraseña";
    }

    // Definimos las variables de uso
    string password = "";
    int a;

    // Inicializamos los números aleatorios
    srand(time(NULL));

    // Cuando se acepta todo en la contraseña
    if (upercase && numbers && symbols){
        for (int i=0; i<length; i++){
            a = 33 + rand() % (127 - 33); // Número aleatorio entre 33 y 126 (ASCII)
            password = password + char(a);
        }
        return password;
    }

    // Cuando aceptamos números y mayúsculas
    if (upercase && numbers){
        for (int i=0; i<length; i++){
            a = 48 + rand() % (123 - 48); // Número aleatorio entre 48 y 122 (ASCII)
            while ((a>=58 && a<=64) || (a>=91 && a<=96)){
                a = 48 + rand() % (123 - 48); // Pedimos a hasta que esté en esos números porque sino serían símbolos.
            }
            password = password + char(a);
        }
        return password;
    }

    // Cuando aceptamos números y símbolos
    if (symbols && numbers){
        for (int i=0; i<length; i++){
            a = 33 + rand() % (127 - 33); 
            while (a>=65 && a<=90){
                a = 33 + rand() % (127 - 33);
            }
            password = password + char(a);
        }
        return password;
    }

    // Cuando aceptamos mayúsculas y símbolos
    if (symbols && upercase){
        for (int i=0; i<length; i++){
            a = 33 + rand() % (127 - 33); 
            while (a>=48 && a<=57){
                a = 33 + rand() % (127 - 33);
            }
            password = password + char(a);
        }
        return password;
    }

    // Cuando aceptamos solo mayúsculas.
    if (upercase){
        for (int i=0; i<length; i++){
            a = 65 + rand() % (123 - 65); 
            while (a>=91 && a<=96){
                a = 65 + rand() % (123 - 65); 
            }
            password = password + char(a);
        }
        return password;
    }

    // Cuando aceptamos solo símbolos
    if (symbols){
        for (int i=0; i<length; i++){
            a = 33 + rand() % (127 - 33); 
            while ((a>=48 && a<=57) || (a>=65 && a<=90)){
                a = 33 + rand() % (127 - 33);
            }
            password = password + char(a);
        }
        return password;
    }

    // Cuando aceptamos solo números
    if (numbers){
        for (int i=0; i<length; i++){
            a = 48 + rand() % (123 - 48); 
            while (a>=58 && a<=96){
                a = 48 + rand() % (123 - 48);
            }
            password = password + char(a);
        }
        return password;
    }

    // Cuando no aceptamos nada
    if (numbers == false && upercase == false && symbols == false){
        for (int i=0; i<length; i++){
            a = 97 + rand() % (123 - 97); 
            password = password + char(a);
        }
        return password;
    }
}

int main(){
    string password;

    password = PasswordGenerator(8, true, true, true);
    cout<<"Contraseña 1: "<<password<<endl<<endl;
    password = PasswordGenerator(9, true, true, false);
    cout<<"Contraseña 2: "<<password<<endl<<endl;
    password = PasswordGenerator(10, true, false, true);
    cout<<"Contraseña 3: "<<password<<endl<<endl;
    password = PasswordGenerator(11, false, false, true);
    cout<<"Contraseña 4: "<<password<<endl<<endl;
    password = PasswordGenerator(12, false, false, false);
    cout<<"Contraseña 5: "<<password<<endl<<endl;
    password = PasswordGenerator(12, false, true, true);
    cout<<"Contraseña 6: "<<password<<endl<<endl;

    return 0;
}
