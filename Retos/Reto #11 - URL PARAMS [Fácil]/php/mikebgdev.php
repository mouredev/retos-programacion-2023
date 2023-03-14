<?php

declare(strict_types=1);

function getParamsUrl(string $url): array
{
    $urlParts = explode('?', $url);
    $arrValues = [];

    if (!isset($urlParts[1])){
        return $arrValues;
    }

    foreach(explode('&', $urlParts[1]) as $param){
        $arrParams = explode('=', $param);
        $arrValues[$arrParams[0]] = $arrParams[1] ?? '';
    }

    return $arrValues;
}

function printValues (array $params): void
{
    if(empty($params)){
        echo 'No tiene argumentos'.PHP_EOL;
    }

    foreach($params as $param => $value){
        echo 'Argumento: '.$param. ' con valor: '. $value .PHP_EOL;
    }
}

$url1 = "https://retosdeprogramacion.com?year=2023&challenge=0";
$url2 = "https://retosdeprogramacion.com?empty";
$url3 = "https://retosdeprogramacion.com";

printValues(getParamsUrl($url1));
printValues(getParamsUrl($url2));
printValues(getParamsUrl($url3));

?>