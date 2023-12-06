<?php
    foreach(range(1,100) as $numero){
        $fizz = ($numero % 3 == 0) ? true : false;
        $buzz = ($numero % 5 == 0) ? true : false;
        
        if($fizz && $buzz){
            print "$numero es un fizzbuzz";
        }elseif($fizz){
            print "$numero es un fizz";
        }elseif($buzz){
            print "$numero es un buzz";
        }else{
            print "$numero no es Nada";
        }
        print "\n";
    }