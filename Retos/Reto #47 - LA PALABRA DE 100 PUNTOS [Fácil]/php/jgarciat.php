<?php

/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */


 $letras = array('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z');

$valoresLetras = range(1, 27);

$asociacion = array_combine($letras, $valoresLetras);

function countPoints($palabra, $asociacion) {
 $palabra = strtoupper($palabra);

 $puntos = 0;

 for ($i = 0; $i < strlen($palabra); $i++) {
     $letra = $palabra[$i];

     if (isset($asociacion[$letra])) {
         $puntos += $asociacion[$letra];
     }
 }

 return $puntos;
}

$palabra = "ZAMBRANO"; // Cambia la palabra y mira cuántos puntos consigues
$puntosPalabra = countPoints($palabra, $asociacion);
$totalPuntos = $puntosPalabra;

echo "La palabra '$palabra' tiene un valor de puntos de: $puntosPalabra\n";

if ($totalPuntos == 100) {
 echo "¡Felicidades! Has alcanzado 100 puntos. El programa finaliza.\n";
}



?>