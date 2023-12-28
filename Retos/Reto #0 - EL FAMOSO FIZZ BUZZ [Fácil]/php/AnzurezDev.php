<?php
function fizz_buzz() {
    for ( $index=1; $index<=100; $index++ ) {
        $output = ( $index % 3 ==0 ? "fizz" : "" ) . ( $index % 5 ==0 ? "buzz" : "");
        $output = $output ? $output : $index;
        echo $output . "\n";
    }
}

fizz_buzz();