#!/bin/bash

# funciones

EsPrimo() {
  num=$1
  EsPrimo=1
  for ((i=2; i<=$((num/2)); i++)); do
    if [ $((num % i)) -eq 0 ]; then
      EsPrimo=0
      break
    fi
  done
  echo $EsPrimo
}

EsFibonacci() {
  num=$1
  EsFibonacci=0
  fib1=0
  fib2=1
  while [ $fib1 -lt $num ]; do
    fib3=$((fib1 + fib2))
    fib1=$fib2
    fib2=$fib3
    if [ $fib1 -eq $num ]; then
      EsFibonacci=1
      break
    fi
  done
  echo $EsFibonacci
}
 
EsParImpar() {
  num=$1
  if [ $((num % 2)) -ne 0 ]; then
    echo 1
  else
    echo 0
  fi
}

# Solicitar numero
echo "Ingresa un número:"
read num

# cadena resultado
string="$num "

# numero es primo o no
EsPrimo=$(EsPrimo $num)
if [ $EsPrimo -eq 1 ]; then
  string="$string es primo, "
else
  string="$string no es primo, "
fi

# numero es fibonacci o no
EsFibonacci=$(EsFibonacci $num)
if [ $EsFibonacci -eq 1 ]; then
  string="$string es fibonacci, "
else
  string="$string no es fibonacci, "
fi

# numero es par o impar
EsParImpar=$(EsParImpar $num)
if [ $EsParImpar -eq 1 ]; then
  string="$string es impar"
else
  string="$string es par"
fi

# Imprimir el resultado
echo $string
