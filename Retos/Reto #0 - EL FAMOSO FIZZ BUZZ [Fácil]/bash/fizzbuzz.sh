#!/bin/bash
contador=1
fin=100
while [ $fin -ge $contador ]
do
  if [[ $(($contador % 3)) == 0 ]] && [[ $(($contador % 5)) == 0 ]]
  then
      echo "fizzbuzz"
  elif  [[ $(($contador % 5)) == 0 ]]
  then
      echo "buzz"
  elif [[ $(($contador % 3)) == 0 ]]
  then
      echo "fizz"
  fi
  let contador++
done
