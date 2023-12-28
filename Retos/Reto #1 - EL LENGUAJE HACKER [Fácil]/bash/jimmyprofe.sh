#!/bin/bash

contenido="El lenguaje hacker"

str=$(echo $contenido | tr '[:upper:]' '[:lower:]' | tr ' ' '+')
echo $str | tr '+' ' '
#str="JIMMYPROFE"; $(echo $(str) | tr '[:upper:]' '[:lower:]')

declare -a palabra
declare -a pa_hack

for ((i=0; i<=${#str}; i++))
{
  palabra=("${palabra[@]}" ${str:i:1})
}
#echo "${palabra[@]}"

function dicc()
{
  declare -A codigo
  codigo[a]='4'
  codigo[b]='I3'
  codigo[c]='{'
  codigo[d]=')'
  codigo[e]='3'
  codigo[f]='|='
  codigo[g]='&'
  codigo[h]='#'
  codigo[i]='1'
  codigo[j]=',_|'
  codigo[k]='>|'
  codigo[l]='1'
  codigo[m]='/\/\'
  codigo[n]='^/'
  codigo[o]='0'
  codigo[p]='|*'
  codigo[q]='(_,)'
  codigo[r]='I2'
  codigo[s]='5'
  codigo[t]='7'
  codigo[u]='(_)'
  codigo[v]='\/'
  codigo[w]='\/\/'
  codigo[x]='><'
  codigo[y]='j'
  codigo[z]='2'
  codigo[+]='+'
  codigo[1]='L'
  codigo[2]='R'
  codigo[3]='E'
  codigo[4]='A'
  codigo[5]='S'
  codigo[6]='b'
  codigo[7]='T'
  codigo[8]='B'
  codigo[9]='g'
  codigo[0]='o'

  for ((j=0; j<${#str}; j++))
  {
  pa_hack=("${pa_hack[@]}" ${codigo[${palabra[j]}]})
  }
}
dicc

result1=$(echo "${pa_hack[@]}" | tr -d '[[:space:]]')
#echo $result1
result2=$(echo $result1 | tr '+' ' ')
echo $result2