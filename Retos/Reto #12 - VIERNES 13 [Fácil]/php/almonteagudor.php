<?php

function check(int $month, int $year)
{
    if (!checkdate($month, 13, $year)) die("Fecha no válida");

    $datetime = DateTime::createFromFormat("d/m/Y", "13/$month/$year");

    return "Friday" === $datetime->format("l");
}

foreach (range(1, 12) as $month) {
    echo("El $month/2023 " . (check($month, 2023) ? "contiene" : "no contiene") . " Viernes 13\n");
}
