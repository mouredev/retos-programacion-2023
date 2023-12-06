<?php
    function isHeterogram($cadena) {
        $cadena = removeDiacritics(mb_strtolower($cadena));
        if (mb_strlen($cadena) == count(array_unique(str_split($cadena))))
            echo "true\n";
        else
            echo "false\n";
    }

    function isIsogram($cadena) {
        $letras_vistas = array();
        foreach (str_split(removeDiacritics($cadena)) as $letra) {
            if (in_array($letra, $letras_vistas)) {
                echo "false\n";
                return;
            }
            array_push($letras_vistas, $letra);
        }
        echo "true\n";
        return true;
    }

    function isPangram($cadena) {
        $alfabeto = str_split('abcdefghijklmnopqrstuvwxyz');
        $cadena = removeDiacritics(strtolower($cadena));
        foreach (str_split($cadena) as $letra) {
            if (in_array($letra, $alfabeto)) {
                $key = array_search($letra, $alfabeto);
                unset($alfabeto[$key]);
            }
            if (empty($alfabeto)) {
                echo "true\n";
                return ;
            }
        }
        echo "false\n";
        return false;
    }

function removeDiacritics($cadena) {
    $diacriticos = array(
                            'á' => 'a', 'é' => 'e', 'í' => 'i', 'ó' => 'o', 'ú' => 'u',
                            'à' => 'a', 'è' => 'e', 'ì' => 'i', 'ò' => 'o', 'ù' => 'u',
                            'ä' => 'a', 'ë' => 'e', 'ï' => 'i', 'ö' => 'o', 'ü' => 'u',
                            'â' => 'a', 'ê' => 'e', 'î' => 'i', 'ô' => 'o', 'û' => 'u',
                            'ã' => 'a', 'ñ' => 'n', 'õ' => 'o',
                            'ç' => 'c'
                        );
    $cadena_sin_diacriticos = strtr($cadena, $diacriticos);
    return $cadena_sin_diacriticos;
}

$string1 = "murcielago";
$string2 = "esdrújula";
$string3 = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de
paja";

isHeterogram($string1); // true
isHeterogram($string2) . "\n"; // false
isIsogram($string1) . "\n"; // true
isIsogram($string2) . "\n"; // false
isPangram($string3) . "\n"; // true
?>