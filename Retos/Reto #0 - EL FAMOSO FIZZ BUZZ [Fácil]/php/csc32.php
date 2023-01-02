<?php 
function fizzbuzz($num){
    if ($num % 3 == 0 && $num % 5 == 0){
       return  "fizzbuzz";
    }

    if ($num % 3 == 0 ){
       return  "fizz";
    }

    if ($num % 5 == 0){
       return  "buzz";
    }
    return $num;
}

for ($i=1; $i <101 ; $i++) { 
   echo fizzbuzz($i) . "\n";
}
?>