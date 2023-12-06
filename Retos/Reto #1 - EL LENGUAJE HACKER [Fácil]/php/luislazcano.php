<?php
    $palabra = trim($argv[1]);
    if($palabra <> ''){
        $map = ["a" => "4","b" => "8","c" => "(","d" => "[)","e" => "3","f" => "|=","g" => "6","h" => "|-|","i" => "!","j" => "_|","k" => "k","l" => "|_","m" => "|v|","n" => "()","o" => "0","p" => "|*","q" => "0_","r" => "|2","s" => "5","t" =>"7","u" => "|_|","v" => "\/","w" => '\/\/',"x" => "%","y" => "`/","z" => "7_",'1' => 'L','2' => 'R','3' => 'E','4' => 'A','5' => 'S','6' => 'b','7' => 'T','8' => 'B','9' => 'g','0' => 'o'];
        $nuevaPalabra = '';
        foreach(range(0,strlen($palabra)) as $indice){
            $caracter = strtolower(substr($palabra,$indice,1));
            $nuevaPalabra = $nuevaPalabra . (isset($map[$caracter]) ? $map[$caracter] : $caracter);
        }
        print $nuevaPalabra . "\n";
    } else{ 
        print 'Deber usar php luislazcano.php <frase>' . "\n";
    }


