<?php

    function generarPasswords($longitud = 12, $usarMayuscula = false, $usarNumeros = false, $usarSimbolos = false)
    {
        $caracteres = 'abcdefghijklmnopqrstuvwxyz';
        $mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $numeros = '0123456789';
        $simbolos = '!@#$%^&*()_-=+{}[]\|;:,.<>?';

        $longitud = $longitud > 16 ? 16 : ($longitud < 8 ? 8 : $longitud);
            
        if ($usarMayuscula) {
            $caracteres .= $mayusculas;
        }
        if ($usarNumeros) {
            $caracteres .= $numeros;
        }
        if ($usarSimbolos) {
            $caracteres .= $simbolos;
        }
        
        $password = '';
        $lenCaracteres = strlen($caracteres);

        for ($i = 0; $i < $longitud; $i++) {
            $randomChar = rand(0, $lenCaracteres - 1);
            $password .= $caracteres[$randomChar];
        }

        return $password;
    }
    
    echo generarPasswords() . "\n";
    echo generarPasswords(8, true, true, true) . "\n";
    echo generarPasswords(12, true, true, true) . "\n";
    echo generarPasswords(16, true, true, true) . "\n";
    echo generarPasswords(12, false, true, true) . "\n";
    echo generarPasswords(12, true, false, true) . "\n";
    echo generarPasswords(12, true, true) . "\n";
    echo generarPasswords(20, false, false, true) . "\n";
    echo generarPasswords(4, false, false, true) . "\n";
?>