<?php

function decimalToOctal($decimal) {
    $numero = $decimal;
    $octal = 0;
    $i = 1;
    while ($decimal != 0) {
        $remainder = $decimal % 8;
        $decimal = floor($decimal / 8);
        $octal += $remainder * $i;
        $i *= 10;
    }
    return "El numero $numero en base decimal corresponde al numero $octal en base octal\n";
}


function decimalToHexadecimal($decimal) {
    $numero = $decimal;
    $hexadecimal = '';
    while ($decimal != 0) {
        $remainder = $decimal % 16;
        if ($remainder < 10) {
        $hexadecimal = chr($remainder + 48) . $hexadecimal;
        } else {
        $hexadecimal = chr($remainder + 55) . $hexadecimal;
        }
        $decimal = floor($decimal / 16);
    }
    return "El numero $numero en base decimal corresponde al numero $hexadecimal en base hexadecimal\n";
}


echo decimalToOctal(25);
echo decimalToHexadecimal(255);
?>