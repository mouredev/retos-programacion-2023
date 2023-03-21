/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

#include <bits/stdc++.h>
using namespace std;

int main(){

   int p1_points=0,p2_points=0;

    string jugada1="",jugada2="";

    cin >> jugada1 >> jugada2;

    if (jugada1==jugada2){
        p1_points=p2_points;
    }else if (jugada1=="🗿" && (jugada2=="✂️" || jugada2=="🦎")){
        p1_points++;
    }else if (jugada1=="📄" && (jugada2=="🗿" || jugada2=="🖖")){
        p1_points++;
    }else if (jugada1=="✂️" && (jugada2=="📄" || jugada2=="🦎")){
        p1_points++;
    }else if (jugada1=="🦎" && (jugada2=="📄" || jugada2=="🖖")){
        p1_points++;
    }else if (jugada1=="🖖" && (jugada2=="✂️" || jugada2=="🗿")){
        p1_points++;
    }else if (jugada2=="🗿" && (jugada1=="✂️" || jugada1=="🦎")){
        p2_points++;
    }else if (jugada2=="📄" && (jugada1=="🗿" || jugada1=="🖖")){
        p2_points++;
    }else if (jugada2=="✂️" && (jugada1=="📄" || jugada1=="🦎")){
        p2_points++;
    }else if (jugada2=="🦎" && (jugada1=="📄" || jugada1=="🖖")){
        p2_points++;
    }else if (jugada2=="🖖" && (jugada1=="✂️" || jugada1=="🗿")){
        p2_points++;
    }

    if (p1_points>p2_points){
        cout << "Player 1" << endl;
    }else if (p2_points>p1_points) {
        cout << "Player 2" << endl;
    }else {
        cout << "Tie" << endl;
    }

}

// 🗿 -> ✂️ && 🦎
// 📄 -> 🗿 && 🖖
// ✂️ -> 📄 && 🦎
// 🦎 -> 📄 && 🖖
// 🖖 -> ✂️ && 🗿

/*
 string juego="";

    int p1_points=0,p2_points=0;

    vector<pair <string, string>> jugadas = {
        {"🗿","📄"},
        {"🗿","🗿"},
        {"🗿","✂️"},
        {"🗿","🦎"},
        {"🗿","🖖"},
        {"📄","🗿"},
        {"📄","📄"},
        {"📄","✂️"},
        {"📄","🦎"},
        {"📄","🖖"},
        {"✂️","🗿"},
        {"✂️","📄"},
        {"✂️","✂️"},
        {"✂️","🖖"},
        {"✂️","🦎"},
        {"🗿","🖖"},
        {"🦎","🗿"},
        {"🦎","🦎"},
        {"🦎","✂️"},
        {"🦎","📄"},
        {"🦎","🖖"},
        {"🖖","✂️"},
        {"🖖","📄"},
        {"🖖","🖖"},
        {"🖖","🦎"},
        {"🖖","🗿"}
        };
    
    pair<string, string> jugada1= jugadas[0];
    pair<string, string> jugada2= jugadas[1];
    pair<string, string> jugada3= jugadas[2];
    pair<string, string> jugada4= jugadas[3];
    pair<string, string> jugada5= jugadas[4];
    pair<string, string> jugada6= jugadas[5];
    pair<string, string> jugada7= jugadas[6];
    pair<string, string> jugada8= jugadas[7];
    pair<string, string> jugada9= jugadas[8];
    pair<string, string> jugada10= jugadas[9];
    pair<string, string> jugada11= jugadas[10];
    pair<string, string> jugada12= jugadas[11];
    pair<string, string> jugada13= jugadas[12];
    pair<string, string> jugada14= jugadas[13];
    pair<string, string> jugada15= jugadas[14];
    pair<string, string> jugada16= jugadas[15];
    pair<string, string> jugada17= jugadas[16];
    pair<string, string> jugada18= jugadas[17];
    pair<string, string> jugada19= jugadas[18];
    pair<string, string> jugada20= jugadas[19];
    pair<string, string> jugada21= jugadas[20];
    pair<string, string> jugada22= jugadas[22];
    pair<string, string> jugada23= jugadas[22];
    pair<string, string> jugada24= jugadas[23];
    pair<string, string> jugada25= jugadas[24];
*/