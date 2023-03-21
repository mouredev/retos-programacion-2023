/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

#include <bits/stdc++.h>
using namespace std;

int main(){
int P1=0,P2=0,t=0;

  string p;

  cin >> p;

  while (t==0){
    
      if (p=="P1" && P1==0 && P2==0){
        P1=15;
        cout << P1 << " - Love" << endl;
      }else if (p== "P1" && P1==15 && P2==0){
        P1=30;
        cout << P1 << " - Love";
      }else if (p=="P1" && P1==30 && P2==0){
        P1=40;
        cout  << P1 << " - Love" << endl;
      }else if (p== "P1" && P1==40 && P2==0){
        cout << "Ha ganado el P1" << endl;
        t=1;
      }else if (p== "P1" && P1==15 && P2==15){
        P1 =30;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P1" && P1==30 && P2==15){
        P1=40;
        cout  << P1 << " - " << P2 << endl;
      }else if (p== "P1" && P1==40 && P2==15){
        cout << "Ha ganado el P1";
        t=1;
      }else if (p== "P1" && P1==15 && P2==30){
        P1=30;
        cout << P1 << " - " << P2;
      }else if (p=="P1" && P1==30 && P2==30){
        P1=40;
        cout  << P1 << " - " << P2 << endl;
      }else if (p== "P1" && P1==40 && P2==30){
        cout << "Ha ganado el P1" << endl;
        t=1;
      }else if (p== "P1" && P1==15 && P2==40){
        P1=30;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P1" && P1==30 && P2==40){
        P1=40;
        cout  <<"Deuce" << endl;
      }else if (p== "P1" && P1==40 && P2==40){
        P1=55;
        cout << "Ventaja para P1" << endl;
      }else if (p=="P1" && P1==55){
        cout << "Ha ganado P1" << endl;
        t=1;
      }else if (p=="P2" && P1==0 && P2==0){
        P2=15;
        cout << "Love - " << P2 << endl;
      }else if (p=="P2" && P1==0 && P2==15){
        P2=30;
       cout << "Love - " << P2 << endl;
      }else if (p=="P2" && P1==0 && P2==30){
        P2=40;
        cout << "Love - " << P2 << endl;
      }else if (p=="P2" && P1==0 && P2==40){
        cout << "Ha ganado P2" << endl;
        t=1;
      }else if (p=="P2" && P1==15 && P2==0){
        P2=15;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==15 && P2==15){
        P2=30;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==15 && P2==30){
        P2=40;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==15 && P2==40){
        cout << "Ha ganado P2" << endl;
        t=1;
      }else if (p=="P2" && P1==30 && P2==0){
        P2=15;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==30 && P2==15){
        P2=30;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==30 && P2==30){
        P2=40;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==30 && P2==40){
        cout << "Ha ganado P2" << endl;
        t=1;
      }else if (p=="P2" && P1==40 && P2==0){
        P2=15;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==40 && P2==15){
        P2=30;
        cout << P1 << " - " << P2 << endl;
      }else if (p=="P2" && P1==40 && P2==30){
        P2=40;
        cout << "Deuce" << endl;
      }else if (p=="P2" && P1==40 && P2==40){
        P2=55;
        cout << " Ventaja para P2" << endl;  
      }else if(p=="P2" && P2==55){
        cout << "Ha ganado P2" << endl;
        t=1;
      } 
    cin >> p;
  }
}