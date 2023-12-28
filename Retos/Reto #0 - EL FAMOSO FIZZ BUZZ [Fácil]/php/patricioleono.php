<?php
$cantidad = 100;
for($i = 1; $i <= $cantidad; $i++){
    if ($i % 3 == 0 && $i % 5 == 0){
        echo 'fizzbuzz';
        echo "'\n'";
    }elseif ($i % 5 == 0) {
        echo 'buzz';
        echo "'\n'";
    }elseif($i % 3 == 0){
        echo 'fizz';
        echo "'\n'";
    }else {
        echo $i;
        echo "'\n'"; 
    }
}

?>
