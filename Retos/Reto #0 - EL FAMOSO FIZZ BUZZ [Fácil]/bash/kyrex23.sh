#!/usr/bin/env bash

# # Reto #0: EL FAMOSO "FIZZ BUZZ"
# #### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
#
# ## Enunciado
#
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#
# Author: kyrex23
# Date:   22/01/2023

MIN_VALUE=1
MAX_VALUE=100

FIZZ_DIVISOR=3
BUZZ_DIVISOR=5

for i in $(seq $MIN_VALUE $MAX_VALUE); do
    message=""

    (($i % $FIZZ_DIVISOR == 0)) && message+="fizz"
    (($i % $BUZZ_DIVISOR == 0)) && message+="buzz"
    [ -z "$message" ] && message="$i"

    echo $message
done
