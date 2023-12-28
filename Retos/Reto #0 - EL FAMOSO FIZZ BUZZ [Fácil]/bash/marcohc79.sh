#!/bin/bash

fizzbuzz () {
  for ((i = 1 ; i  <= 100; i++)); do
    if [[ $((i%3)) -eq 0  &&  $((i%5)) -eq 0 ]]; then
      echo "fizzbuzz"
    elif [[ $((i%3)) -eq 0 ]]; then
      echo "fizz"
    elif [ $((i%5)) -eq 0 ]; then
      echo "buzz"
    else
      echo "$i"
    fi
  done
}

fizzbuzz
