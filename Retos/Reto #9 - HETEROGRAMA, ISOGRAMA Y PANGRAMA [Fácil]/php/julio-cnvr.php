<?php

function esHeterograma($string) {
    $esHeterograma = false;

    //quitamos espacios en blanco y signos de puntuación de la cadena
    $str = str_replace(" ", "", $string);
    $str = str_replace(";", "", $str);
    $str = str_replace(",", "", $str);
    $str = str_replace(".", "", $str);

    //soporte para vocales acentuadas y la ü
    $str = str_replace("á","a", $str);
    $str = str_replace("é","e", $str);
    $str = str_replace("í","i", $str);
    $str = str_replace("ó","o", $str);
    $str = str_replace("ú","u", $str);
    $str = str_replace("Á","A", $str);
    $str = str_replace("É","E", $str);
    $str = str_replace("Í","I", $str);
    $str = str_replace("Ó","O", $str);
    $str = str_replace("Ú","U", $str);
    $str = str_replace("ü","u", $str);
    $str = str_replace("Ü","U", $str);
    

    //soporte para la Ñ
    $str = str_replace("ñ", "Ñ", $str); 

    //convertimos toda la cadena en mayusculas y contamos la ocurrencia de cada caracter
    $str = strtoupper($str);
    $arrayString = mb_count_chars($str);
    
    //sumamos los valores de los contadores
    $longitudCadena = 0;
    $suma = 0;
    foreach ($arrayString as $key => $value) {
        $suma = $suma + $value;
        $longitudCadena++;
    }

    //si la suma de los contadores es igual a la longitud de la cadena, entonces
    //es un Heterograma, ya que todos los contadores tendran el valor 1
    if ($suma == $longitudCadena) {
        $esHeterograma = true;
    }
    return $esHeterograma;
}

function esPangrama ($string) {
    $esPangrama = false;

    //quitamos espacios en blanco y signos de puntuación de la cadena
    $str = str_replace(" ", "", $string);
    $str = str_replace(";", "", $str);
    $str = str_replace(",", "", $str);
    $str = str_replace(".", "", $str);
    
    //soporte para vocales acentuadas y la ü
    $str = str_replace("á","a", $str);
    $str = str_replace("é","e", $str);
    $str = str_replace("í","i", $str);
    $str = str_replace("ó","o", $str);
    $str = str_replace("ú","u", $str);
    $str = str_replace("Á","A", $str);
    $str = str_replace("É","E", $str);
    $str = str_replace("Í","I", $str);
    $str = str_replace("Ó","O", $str);
    $str = str_replace("Ú","U", $str);
    $str = str_replace("ü","u", $str);
    $str = str_replace("Ü","U", $str);
    
    //convertimos toda la cadena en mayusculas y contamos la ocurrencia de cada caracter
    $str = strtoupper($str);
    $countArray = mb_count_chars($str);

    //si hay 27 contadores, entonces la cadena tiene todas las letras del alfabeto
    if (count($countArray) == 27) {
        $esPangrama = true;
    }
    return $esPangrama;
}

function esIsograma($string) {
    $esIsograma = true;

    //quitamos espacios en blanco y signos de puntuación de la cadena
    $str = str_replace(" ", "", $string);
    $str = str_replace(";", "", $str);
    $str = str_replace(",", "", $str);
    $str = str_replace(".", "", $str);
    
    //soporte para vocales acentuadas y la ü
    $str = str_replace("á","a", $str);
    $str = str_replace("é","e", $str);
    $str = str_replace("í","i", $str);
    $str = str_replace("ó","o", $str);
    $str = str_replace("ú","u", $str);
    $str = str_replace("Á","A", $str);
    $str = str_replace("É","E", $str);
    $str = str_replace("Í","I", $str);
    $str = str_replace("Ó","O", $str);
    $str = str_replace("Ú","U", $str);
    $str = str_replace("ü","u", $str);
    $str = str_replace("Ü","U", $str);

    //convertimos toda la cadena en mayusculas y contamos la ocurrencia de cada caracter
    $str = strtoupper($str);
    $countArray = mb_count_chars($str);

    //almacenamos el valor de los contadores en un array $counts
    $counts = [];
    $i = 0;
    foreach ($countArray as $key => $value) {
        $counts[$i] = $value;
        $i++;
    }

    //verificamos si todos los contadores tienen el mismo valor
    //si cualquiera es diferente entonces no es un Isograma
    $i = 0;
    foreach ($counts as $value) {
        $valorComp = $value;
        if (($i+1) < count($counts)) {
            if ($valorComp != $counts[$i+1]) {
                $esIsograma = false;
                break;
            }
        }
        $i++;
    }
    return $esIsograma;
}

function mb_count_chars($string) {
    $len = mb_strlen($string, 'UTF-8');
    $unique = array();
    for($i = 0; $i < $len; $i++) {
        $char = mb_substr($string, $i, 1, 'UTF-8');
        if(!array_key_exists($char, $unique))
            $unique[$char] = 0;
        $unique[$char]++;
    }
    return $unique;
}

//$heterograma = "Uno de mis, tu"; 

//$pangrama = "Benjamín pidió una bebida de Kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.";
//$pangrama2 = "abcde fghij, klmnñ opqrs; tuvwx yzzzzz";

//$isograma = "ddgg, hihi;jjkk.ñ";
