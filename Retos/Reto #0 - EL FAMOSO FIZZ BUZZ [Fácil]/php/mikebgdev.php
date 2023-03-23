<?php

    function fizzBuzz ($num):string
    {
        if ($num % 3 == 0) {
            return ($num % 5 == 0) ? "fizzbuzz" : "fizz";
        }

        return ($num % 5 == 0) ? "buzz" : "{$num}";
    }

    for ($i = 1; $i <= 100; $i++){
        echo fizzBuzz($i) . "\n";
    }

?>