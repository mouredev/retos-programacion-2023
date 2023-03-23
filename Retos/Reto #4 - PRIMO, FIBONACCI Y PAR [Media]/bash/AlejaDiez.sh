#!/bin/bash

# Si es divisible entre dos es par
function esPar() {
    local num=$1

    if [[ $(($num % 2)) = 0 ]]; then
        echo "si"
    else
        echo "no"
    fi
}

function esPrimo() {
    local num=$1
    local esPrimo=1

    if [[ $num -lt  2 ]]; then # Los números menores a 2 no son primos
        esPrimo=0
    elif [[ $num != 2 && $(esPar $num) = "si" ]]; then # Los números pares excepto el 2 no son primos
        esPrimo=0
    else
        for (( i=3; i<$num; i++ )); do # Si es divisible por algún número anterior no es primo
            if [[ $(($num % $i)) = 0 ]]; then
                esPrimo=0
                break
            fi
        done
    fi
    if [[ $esPrimo = 1 ]]; then
        echo "si"
    else
        echo "no"
    fi
}

function esFibonacci() {
    local num=$1
    local num1=0
    local num2=1
    local esFibonacci=1

    while [[ $num1 != $num ]]; do
        if [[ $num1 -gt $num ]]; then
            esFibonacci=0
            break
        else
            suma=$(($num1 + $num2))
            num1=$num2
            num2=$suma
        fi
    done
    # Comprobación de que el número no es fibonacci
    if [[ $esFibonacci = 1 ]]; then
        echo "si"
    else
        echo "no"
    fi
}

declare numero

echo -n "Introduce un número: "
read numero
# Comprobación de que es un entero
if [[ $numero =~ ^[0-9]+$ ]]; then
    echo "  - Es par:" $(esPar $numero)
    echo "  - Es primo:" $(esPrimo $numero)
    echo "  - Es Fibonacci:" $(esFibonacci $numero)
else
    echo "Tienes que introducir un número entero."
fi
