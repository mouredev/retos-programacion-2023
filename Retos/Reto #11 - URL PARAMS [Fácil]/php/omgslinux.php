<?php

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */


$URLS = [
    'https://retosdeprogramacion.com?year=2023&challenge=0',
    'https://www.youtube.com/watch?v=TedBu1kt5kk',
    'https://www.palabreto.com/'
];

$contador = 0;
foreach ($URLS as $URL) {
    $contador++;
    printf("URL %d: %s\n", $contador, $URL);
    $strip = explode('?', $URL);
    if (count($strip)>1) {
        $args = explode('&', $strip[1]);
        $c = 0;
        foreach ($args as $string) {
            $c++;
            $param = explode('=', $string);
            printf("argumento %d: %s, valor: %s\n", $c, $param[0], $param[1]);
        }
    } else {
        printf("La URL %s no tiene argumentos\n", $URL);
    }
}
