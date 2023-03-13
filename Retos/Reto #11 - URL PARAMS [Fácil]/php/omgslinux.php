<?php

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */

$URL = "https://retosdeprogramacion.com?year=2023&challenge=0";

$strip = explode('?', $URL);
$args = explode('&', $strip[1]);

foreach ($args as $string) {
    $param = explode('=', $string);
    printf("clave: %s, valor: %s\n", $param[0], $param[1]);
}
