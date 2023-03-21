<?php
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

const DOG_API_ENDPOINT = "https://dog-api.kinduff.com/api/facts";
function request() {
    $response = file_get_contents(DOG_API_ENDPOINT);
    $obj = json_decode($response);
    print $obj->{'facts'}[0];
}

request();
