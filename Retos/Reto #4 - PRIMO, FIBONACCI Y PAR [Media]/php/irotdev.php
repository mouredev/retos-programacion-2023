<?php
/**
 * Reto4 of MoureDev: https://github.com/mouredev/retos-programacion-2023/tree/main/Retos/Reto%20%234%20-%20PRIMO%2C%20FIBONACCI%20Y%20PAR%20%5BMedia%5D
 * Check if some numbers are "primo" (prime number), "fibonacci" or "par" (even number).
 * (BONUS*) -> Function for do a list of prime numbers and function for show the list of prime numbers.
 * (IMPORTANT*) -> For check only some numbers, you can use isPrimo(..) without changes, but if you are going to use it
 *      with a lot of numbers (1000 or more) --> rewrite and use listOfPrimeNumbers(..) only once.
 * (BONUS*2) -> Adding function "isPrimo2(..)" checking if a number is a prime number using a different method.
 * @author José Manuel Muñoz Simó | irotdev
 * @version v1.1
 */

CONST NUMBERSTOCHECK = 5;
CONST MAXNUMBER = 1000;


checkRandomListOfNumbers(NUMBERSTOCHECK, MAXNUMBER);
showListOfPrimeNumbers(MAXNUMBER);

function checkRandomListOfNumbers($numbersToCheck, $maxNumber) {
    for ($i = 0; $i < $numbersToCheck; $i++) {
        $num = rand(1, $maxNumber);

        echo $num . " -> ";
        echo "<br> Fibo_? " . (isFibonacci($num) ? "FIBONACCI" : "NO FIBONACCI");
        //echo "<br> Primo? " . (isPrimo($num, $maxNumber) ? "PRIMO" : "NO PRIMO");
        echo "<br> PriV2? " . (isPrimo2($num) ? "PRIMO" : "NO PRIMO");
        echo "<br> Par__? " . (isPar($num) ? "PAR" : "IMPAR" ) . "<br><br>";
    }
}


function isFibonacci($num): bool {
    $sumFiboNum = $prevFiboNum = 1;
    while ($sumFiboNum <= $num)  {
        if ($sumFiboNum == $num) return true;
        $newLastFiboNum = $sumFiboNum;
        $sumFiboNum = $prevFiboNum + $sumFiboNum;
        $prevFiboNum = $newLastFiboNum;
    }
    return false;
}


function isPrimo($num, $maxNumberToCheck): bool {
    // If only check a number, it is ok to call to get the array
    // However, if you are going to check a lot of numbers, save this list in a global variable and call only once
    $listPrimeNumbers =  listOfPrimeNumbers($maxNumberToCheck);

    foreach ($listPrimeNumbers as $numPrime)
        if ($num == $numPrime)
            return true;

    return false;
}

// Without list of prime numbers but checking all the numbers
function isPrimo2($num) {
    for ($i = 2; $i <= sqrt($num); $i++)
        if ($num % $i == 0)
            return false;

    return true;
}


function isPar($num): bool {
    return ($num % 2 == 0);
}


function listOfPrimeNumbers($numMaxToCheck): array {
    $ar = array();
    $ar[] = 2;
    for ($i = 3; $i <= $numMaxToCheck; $i++) {
        $isPrime = true;
        foreach ($ar as $value) {
            if ($i % $value == 0) {
                $isPrime = false;
                break;
            }
        }
        if ($isPrime) $ar[] = $i;   // Add a new number prime
    }
    return $ar;
}


function showListOfPrimeNumbers($numMaxToCheck) {
    $listPrimeNumbers =  listOfPrimeNumbers($numMaxToCheck);
    foreach ($listPrimeNumbers as $value)
        echo $value . " ";
}