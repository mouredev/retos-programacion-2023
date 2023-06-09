<?php


/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */


function checkF13($datemy): bool
{
    $items = explode('/', $datemy);
    list ($month, $year) = $items;
    $date = new DateTime($month . '/13/' . $year);
    // El viernes es el dia 5
    return $date->format('w') == 5;
}

// Ponemos las fechas en formato mm/YYYY
$fechas = [
    '03/2023',
    '01/2023', //si
    '05/2022', //si
    '10/2015',
    '12/2020',
    '07/2018', //si
];

foreach ($fechas as $fecha) {
    printf("El 13/%s %s es viernes\n", $fecha, (checkF13($fecha)?'si':'no'));
}
