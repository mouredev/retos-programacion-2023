// Incluir toda la standar library
#include <bits/stdc++.h>

using namespace std;

map <char, string> diccionario = {
   {'a', "4"},
   {'b', "I3"},
   {'c', "["},
   {'d', ")"},
   {'e', "3"},
   {'f', "|="},
   {'g', "&"}, 
   {'h', "#"},
   {'i', "1"},
   {'j', ",_|"},
   {'k', ">|"},
   {'l', "1"},
   {'m', "/\\/\\"},
   {'n', "^/"},
   {'o', "0"},
   {'p', "|*"},
   {'q', "(_,)"},
   {'r', "I2"},
   {'s', "5"},
   {'t', "7"},
   {'u', "(_)"},
   {'v', "\\/"},
   {'w', "\\/\\/"},
   {'x', "><"},
   {'y', "j"},
   {'z', "2"},
   {'1', "L"},
   {'2', "R"},
   {'3', "E"},
   {'4', "A"},
   {'5', "S"},
   {'6', "b"},
   {'8', "T"},
   {'9', "g"},
   {'0', "o"},
   {' ', " "}
};

int main(){
   // Optimizar cin y cout
   cin.tie(nullptr);
   ios_base::sync_with_stdio(false);

   // Guardar la cadena
   string texto;
   getline(cin, texto);

   // Transformar la cadena desde el inicio hasta al final, y reescribir desde el inicio
   transform(texto.begin(), texto.end(), texto.begin(), ::tolower);

   // Recorrer la cadena con un auto iterator
   for(auto caracter:texto){
      auto busqueda = diccionario.find(caracter);
      (busqueda != diccionario.end()) ? cout << busqueda -> second : cout << "";
   }
   return 0;
}