/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo magico de Harry Potter.
 * - De ser posible realizara 5 preguntas (como minimo) a traves de la terminal.
 * - Cada pregunta tendra 4 respuestas posibles (tambien a selecciona una a traves de terminal).
 * - En funcion de las respuestas a las 5 preguntas deberas diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambicion y la astucia.
 */

/*
Preguntas:
    1- ¿Cual de estos rasgos es mas importante para ti en un amigo?
    2- ¿Cual de estos libros te interesaria mas leer?
    3- ¿Cual de estos deportes preferirias jugar?
    4- ¿Que opinas sobre probar nuevos alimentos o platos?
    5- ¿Que opinas sobre viajar a paises desconocidos?
Gryffindor:
    a) Coraje y valentia
    a) Un libro sobre deportes extremos y aventuras 
    a) Escalada en roca o paracaidismo 
    a) Me encanta probar cosas nuevas y diferentes
    a) Me emociona explorar nuevos lugares y culturas
Slytherin:
    b) Ambicion y exito 
    b) Un libro sobre emprendimiento y negocios
    b) Tenis o golf
    b) Solo pruebo cosas nuevas si tienen buena reputacion 
    b) Solo viajaria a paises seguros y con buena reputacion
Ravenclaw:
    c) Inteligencia y curiosidad
    c) Un libro sobre ciencia o tecnologia
    c) Esqui o snowboard
    c) Me gusta probar nuevos sabores y platos de diferentes culturas
    c) Me encanta viajar y descubrir cosas nuevas
Huffepluf:
    d) Honestidad y lealtad
    d) Un libro sobre relaciones y emociones humanas
    d) Natacion o ciclismo
    d) Me gusta comer lo que ya conozco y me gusta 
    d) Me gusta viajar a lugares conocidos o a los que he visitado antes 
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    string test="";
    cout << "¿Quieres comenzar el test? (y/n)"; cin >> test;
    if (test=="y"){
        string r1="",r2="",r3="",r4="",r5="";
        cout << "\nPrimera pregunta" << endl;
        cout << "\n¿Cual de estos rasgos es mas importante para ti en un amigo?" << endl;
        cout << "a) Coraje y valentia" << endl;
        cout << "b) Ambicion y exito " << endl;
        cout << "c) Inteligencia y curiosidad" << endl;
        cout << "d) Honestidad y lealtad" << endl;
        cin >> r1;

        cout << "\nSegunda pregunta" << endl;
        cout << "\n¿Cual de estos libros te interesaria mas leer?" << endl;
        cout << "a) Un libro sobre deportes extremos y aventuras" << endl;
        cout << "b) Un libro sobre emprendimiento y negocios " << endl;
        cout << "c) Un libro sobre ciencia o tecnologia" << endl;
        cout << "d) Un libro sobre relaciones y emociones humanas" << endl;
        cin >> r2;

        cout << "\nTercera pregunta" << endl;
        cout << "\n¿Cual de estos deportes preferirias jugar?" << endl;
        cout << "a) Escalada en roca o paracaidismo " << endl;
        cout << "b) Tenis o golf" << endl;
        cout << "c) Esqui o snowboard" << endl;
        cout << "d) Natacion o ciclismo" << endl;
        cin >> r3;

        cout << "\nCuarta pregunta" << endl;
        cout << "\n¿Que opinas sobre probar nuevos alimentos o platos?" << endl;
        cout << "a) Me encanta probar cosas nuevas y diferentes" << endl;
        cout << "b) Solo pruebo cosas nuevas si tienen buena reputacion " << endl;
        cout << "c) Me gusta probar nuevos sabores y platos de diferentes culturas" << endl;
        cout << "d) Me gusta comer lo que ya conozco y me gusta" << endl;
        cin >> r4;

        cout << "\nQuinta pregunta" << endl;
        cout << "\n¿Que opinas sobre viajar a paises desconocidos?" << endl;
        cout << "a) Me emociona explorar nuevos lugares y culturas" << endl;
        cout << "b) Solo viajaria a paises seguros y con buena reputacion" << endl;
        cout << "c) Me encanta viajar y descubrir cosas nuevas" << endl;
        cout << "d) Me gusta viajar a lugares conocidos o a los que he visitado antes" << endl;
        cin >> r5;

        int gry=0,sly=0,rav=0,huff=0;

        if(r1=="a"){
            gry++;
        }else if(r1=="b"){
            sly++;
        }else if(r1=="c"){
            rav++;
        }else if(r1=="d"){
            huff++;
        }else if(r2=="a"){
            gry++;
        }else if(r2=="b"){
            sly++;
        }else if(r2=="c"){
            rav++;
        }else if(r2=="d"){
            huff++;
        }else if(r3=="a"){
            gry++;
        }else if(r3=="b"){
            sly++;
        }else if(r3=="c"){
            rav++;
        }else if(r3=="d"){
            huff++;
        }else if(r4=="a"){
            gry++;
        }else if(r4=="b"){
            sly++;
        }else if(r4=="c"){
            rav++;
        }else if(r4=="d"){
            huff++;
        }else if(r5=="a"){
            gry++;
        }else if(r5=="b"){
            sly++;
        }else if(r5=="c"){
            rav++;
        }else if(r5=="d"){
            huff++;
        }

        if(gry>sly && gry>rav && gry>huff){
            cout << "\nPerteneces a Gryffindor, felicidades" << endl;
        }else if(sly>gry && sly>rav && sly>huff){
            cout <<"\nPerteneces a Slytherin, felicidades" << endl;
        }else if(rav>gry && rav>sly && rav>huff){
            cout <<"\nPerteneces a Ravenclaw, felicidades" << endl;
        }else if(huff>gry && huff>sly && huff>rav){
            cout <<"\nPerteneces a Hufflepuff, felicidades" << endl;
        }

    }else {
        cout << "Muggle..." << endl;
    }
}