#!/bin/bash

#SECUENCIA:
declare -a secuencia=(P1 P1 P2 P2 P1 P2 P1 P1)
#declare -a secuencia=(P2 P2 P1 P1 P2 P1 P2 P2)
#declare -a secuencia=(P2 P2 P1 P1 P2 P2)
#declare -a secuencia=(P1 P1 P2 P2 P1 P1)

puntaje_p1="love"
puntaje_p2="love"

tamano_secuencia=${#secuencia[@]}

declare -a marcador1
declare -a marcador2

Ganador=''
Empate=''

marcador1=("${marcador1[@]}" $puntaje_p1)
marcador2=("${marcador2[@]}" $puntaje_p1)

for ((i=0; i<$tamano_secuencia; i++))
do
    if [ ${secuencia[i]} == P1 ]; then
      case $puntaje_p1 in
        love)
          puntaje_p1=15
          marcador1=("${marcador1[@]}" $puntaje_p1)
          marcador2=("${marcador2[@]}" $puntaje_p2)
        ;;
        15)
          puntaje_p1=30
          marcador1=("${marcador1[@]}" $puntaje_p1)
          marcador2=("${marcador2[@]}" $puntaje_p2)
        ;;
        30)
          puntaje_p1=40
          marcador1=("${marcador1[@]}" $puntaje_p1)
          marcador2=("${marcador2[@]}" $puntaje_p2)
        ;;
        40)
          if [ "$puntaje_p2" == 30 ] || [ "$puntaje_p2" == 15 ] || [ "$puntaje_p2" == "$love" ]; then
            Ganador=$(echo "Ha ganado P1")
          else 
            
            Empate=$(echo "deuce")
            puntaje_p1=Ad_in_p1
            puntaje_p2=deuce
            marcador1=("${marcador1[@]}" $puntaje_p1)
            marcador2=("${marcador2[@]}" $puntaje_p2)
          fi
        ;;
        Ad_in_p1)
          if [ "$puntaje_p2" == "deuce" ]; then
            Ganador="Ha ganado P1"
          else
            puntaje_p1=40
            puntaje_p2=40
            marcador1=("${marcador1[@]}" $puntaje_p1)
            marcador2=("${marcador1[@]}" $puntaje_p2)
          fi        
        ;;
      esac
    else
      
      case $puntaje_p2 in
        love)
          puntaje_p2=15
          marcador1=("${marcador1[@]}" $puntaje_p1)
          marcador2=("${marcador2[@]}" $puntaje_p2)
        ;;
        15)
          puntaje_p2=30
          marcador1=("${marcador1[@]}" $puntaje_p1)
          marcador2=("${marcador2[@]}" $puntaje_p2)
        ;;
        30)
          puntaje_p2=40
          marcador1=("${marcador1[@]}" $puntaje_p1)
          marcador2=("${marcador2[@]}" $puntaje_p2)
        ;;
        40)
          if [ "$puntaje_p1" == 30 ] || [ "$puntaje_p1" == 15 ] || [ "$puntaje_p1" == "$love" ]; then
            Ganador=$(echo "Ha ganado P2")
          else 
            Empate=$(echo "deuce")
            puntaje_p1="deuce"
            puntaje_p2="Ad_in_p2"
            marcador1=("${marcador1[@]}" $puntaje_p1)
            marcador2=("${marcador2[@]}" $puntaje_p2)
          fi
        ;;
        Ad_in_p2)
          if [ "$puntaje_p1" == deuce ]; then
            Ganador="Ha ganado P2"
          else
            puntaje_p1=deuce
            puntaje_p2=deuce
            marcador1=("${marcador1[@]}" $puntaje_p1)
            marcador2=("${marcador1[@]}" $puntaje_p2)
          fi
        ;;

      esac
    fi
done

tamano_marcador1=${#marcador1[@]}

for ((j=0; j<$tamano_marcador1; j++))
do
  if [ "${marcador1[j]}" == 40 ] && [ "${marcador2[j]}" == 40 ]; then
    
    echo $Empate
  elif [ "${marcador1[j]}" == "Ad_in_p1" ] && [ "${marcador2[j]}" == "deuce" ]; then
    echo "Ventaja P1"
  elif [ "${marcador1[j]}" == "deuce" ] && [ "${marcador2[j]}" == "Ad_in_p2" ]; then
    echo "Ventaja P2"
  else 
    echo ${marcador1[j]} - ${marcador2[j]} 
  fi
done

echo $Ganador
