<?php
/** 
 * Challenge #0 - The famous Fizz Buzz 
 */
const LIMITS = [1, 100];

/**
 * Prints the fizz buzz sequence
 *
 * @param int $from
 * @param int $until
 * @return void
 */
function printFizzBuzzSequence($from, $until) {
    for ($i = $from; $i <= $until; $i ++) {
        // First determinates if the number is multiple of
        $isThreeMultiple = ($i % 3) === 0;
        $isFiveMultiple = ($i % 5) === 0;
        
        // Second generates a string and prints
        echo implode([
            $isThreeMultiple ? 'fizz' : '',
            $isFiveMultiple ? 'buzz' : '',
            ($isThreeMultiple || $isFiveMultiple) ? '' : $i
        ]);

        echo "\n";
    }
}

printFizzBuzzSequence(...LIMITS);
