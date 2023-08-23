<?php
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
 
$texto ="Vamos a probar este ejercicio. Tengo que poner un texto un poco largo ". 
"porque si no, esto no vale para nada. El caso es que no se me ocurre qué poner. ".
"Estoy escribiendo la primera parida que me pasa por la cabeza, qué le vamos a ".
"hacer no soy Cervantes.";
$palabra_longa = 0;
$media = 0;
$suma_total = 0;

//Con str_word_count contamos las palabras. Con el segundo parametro 1,
//lo guardamos en forma de array
$palabras = str_word_count($texto, 1);
echo 'Numero de palabras del texto: '.count($palabras).PHP_EOL;

//Con explode separamos en elementos de array ahi donde haya un punto.
//Hay que restar uno al count porque al final del todo hay un punto y cuenta como 
//elemento vacio.
echo 'Numero de oraciones del texto: '.(count(explode('.', $texto))-1).PHP_EOL;

//Adelante con el bucle. Usemos el array $palabras que ya hemos creado

foreach ($palabras as $palabra) {
	$palabra_longa = strlen($palabra) > strlen($palabra_longa) ? $palabra : $palabra_longa;
	$suma_total += strlen($palabra);
}

echo 'Palabra mas larga: '.$palabra_longa.PHP_EOL;
echo 'Longitud media de palabra: '.($suma_total/count($palabras));

//Arreando!!!