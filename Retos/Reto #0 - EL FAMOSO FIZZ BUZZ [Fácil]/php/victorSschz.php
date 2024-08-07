<?php
for($n=1; $n<=100;$n++){

    $salida = match(true){
        ($n%3===0) && ($n%5===0)=> "FizzBuzz '\n'", 
        ($n%3===0)=> "Fizz '\n'", 
        ($n%5===0)=> "Buzz '\n'",
        default => $n ."'\n'"
    };
    echo $salida;
}
?>