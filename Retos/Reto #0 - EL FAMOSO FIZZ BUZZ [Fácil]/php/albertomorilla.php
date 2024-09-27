<?php
/**
 * Write a program that displays by console (with a print) the numbers 1 to 100 (both included 
 * and with a line break between each print), substituting the following:
 * - Multiples of 3 for the word "fizz".
 * - Multiples of 5 for the word "buzz".
 * - Multiples of 3 and 5 at the same time for the word "fizzbuzz".
 * 
 */

for($i = 1; $i < 100; $i++ ){
    if($i % 3 === 0 && $i % 5 === 0){
        echo $i . " - Fizz Buzz <br/>";
    } else if($i % 3 === 0){
        echo $i . " - Fizz <br/>";
    } else if($i % 5 === 0){
        echo $i . " - Buzz <br/>";
    } else {
        echo $i . "<br/>";
    }
}