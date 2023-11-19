# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */

# estructura de dato con la tabla de equivalencias
declare -A alfabeto
alfabeto[a]='4'
alfabeto[b]='I3'
alfabeto[c]='['
alfabeto[d]=')'
alfabeto[e]='3'
alfabeto[f]='|='
alfabeto[g]='&'
alfabeto[h]='#'
alfabeto[i]='1'
alfabeto[j]=',_|'
alfabeto[k]='>|'
alfabeto[l]='1'
alfabeto[m]='/\/\'
alfabeto[n]='^/'
alfabeto[o]='0'
alfabeto[p]='|*'
alfabeto[q]='(_,)'
alfabeto[r]='I2'
alfabeto[s]='5'
alfabeto[t]='7'
alfabeto[u]='(_)'
alfabeto[v]='\/'
alfabeto[w]='\/\/'
alfabeto[x]='><'
alfabeto[y]='j'
alfabeto[z]='2'
alfabeto[1]='L'
alfabeto[2]='R'
alfabeto[3]='E'
alfabeto[4]='A'
alfabeto[5]='S'
alfabeto[6]='b'
alfabeto[7]='T'
alfabeto[8]='B'
alfabeto[9]='g'
alfabeto[0]='0'
alfabeto[ ]=' '

# 1. Pedir el texto y ambiar todo el texto a minuscula
read -p "Indicar el texto que desea traducir: " texto
texto=${texto,,}

# 2. Recorrer el texto y por cada caracter buscar su equivalencia en la tabla
parsed_texto=""
for ((i=0; i<${#texto}; i++)) {
    parsed_texto+="${alfabeto[${texto:i:1}]}"
}

# 3. Imprimir el texto traducido
echo $parsed_texto
