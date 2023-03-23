/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

/*
a 4
b I3
c [
d )
e 3
f |=
g &
h #
i 1
j ,_|
k >|
l 1
m /\/\
n ^/
o 0
p |*
q (_,)
r I2
s 5
t 7
u (_)
v \/
w \/\/
x ><
y j
z 2
1 L
2 R
3 E
4 A
5 S
6 b
7 T
8 B
9 g
0 o
*/

#include <bits/stdc++.h>
using namespace std;

int main(){

    string t,tH="";
    cin >> t;

    for (int i=0; i<=t.size(); i++){
        switch(t[i]){
            case 'a': tH.push_back('4'); break;
            case 'b': tH.push_back('I'),tH.push_back('3'); break;
            case 'c': tH.push_back('['); break;
            case 'd': tH.push_back(')'); break;
            case 'f': tH.push_back('|'),tH.push_back('='); break;
            case 'g': tH.push_back('&'); break;
            case 'h': tH.push_back('#'); break;
            case 'i': tH.push_back('1'); break;
            case 'j': tH.push_back(','), tH.push_back('_'),tH.push_back('|'); break;
            case 'k': tH.push_back('>'),tH.push_back('|'); break;
            case 'l': tH.push_back('1'); break;
            case 'm': tH.push_back('/'),tH.push_back('\\'); break; 
            case 'n': tH.push_back('^'),tH.push_back('/'); break;
            case 'o': tH.push_back('0'); break;
            case 'p': tH.push_back('|'),tH.push_back('*'); break;
            case 'q': tH.push_back('('),tH.push_back('_'),tH.push_back(','),tH.push_back(')'); break;
            case 'r': tH.push_back('I'),tH.push_back('2'); break;
            case 's': tH.push_back('5'); break;
            case 't': tH.push_back('7'); break;
            case 'u': tH.push_back('('),tH.push_back('_'),tH.push_back(')'); break;
            case 'v': tH.push_back('\\'),tH.push_back('/'); break;
            case 'w': tH.push_back('\\'),tH.push_back('/'),tH.push_back('\\'),tH.push_back('/'); break;
            case 'x': tH.push_back('>'),tH.push_back('<'); break;
            case 'y': tH.push_back('j'); break;
            case 'z': tH.push_back('2'); break;
            case '1': tH.push_back('L'); break;
            case '2': tH.push_back('R'); break;
            case '3': tH.push_back('E'); break;
            case '4': tH.push_back('A'); break;
            case '5': tH.push_back('S'); break;
            case '6': tH.push_back('b'); break;
            case '7': tH.push_back('T'); break;
            case '8': tH.push_back('B'); break;
            case '9': tH.push_back('g'); break;
            case '0': tH.push_back('o'); break;
        }
    }

    cout << tH << endl;

}