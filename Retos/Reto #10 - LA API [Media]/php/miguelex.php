<?php

$url = 'https://rickandmortyapi.com/api/character';


$curl = curl_init();


curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);


$response = curl_exec($curl);


if(curl_errno($curl)) {
    echo 'Error al conectar a la API: ' . curl_error($curl);
    exit;
}

// Decodificar la respuesta JSON de la API
$data = json_decode($response, true);

// Mostrar la lista de personajes
foreach($data['results'] as $character) {
    echo "Nombre:" . $character['name'] . "\n";
}

// Cerrar la conexión de cURL
curl_close($curl);
?>