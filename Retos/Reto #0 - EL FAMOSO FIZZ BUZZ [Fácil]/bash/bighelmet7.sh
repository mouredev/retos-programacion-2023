#!/bin/bash

function fizzbuzz() {
    local n=$1

    for i in $(seq 1 ${n}); do
        if [[ $((i%3)) = 0 && $((i%5)) = 0 ]]; then
           echo "fizzbuzz" 
        elif [[ $((i%3)) = 0 ]]; then
           echo "fizz" 
        elif [[ $((i%5)) = 0 ]]; then
           echo "buzz"
        else
            echo "${i}"
        fi
    done
}

fizzbuzz 100
