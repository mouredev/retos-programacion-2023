<?php

declare(strict_types=1);

$uri = 'https://digimon-api.vercel.app/api/digimon/name/palmon';
$curl = curl_init();

/* The line `curl_setopt(, CURLOPT_URL, );` is setting the URL for the cURL request. It
specifies the endpoint or URL that the request will be sent to. In this case, it sets the URL to
'https://digimon-api.vercel.app/api/digimon/name/palmon'. */
curl_setopt($curl, CURLOPT_URL, $uri);
/* The line `curl_setopt(, CURLOPT_RETURNTRANSFER, true);` is setting the `CURLOPT_RETURNTRANSFER`
option for the cURL request. */
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($curl);
curl_close($curl);

$response = json_decode($response);

echo json_encode($response, JSON_PRETTY_PRINT);
