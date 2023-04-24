<?php
/**
 * Example of use of the AEMET API: https://opendata.aemet.es/centrodedescargas/inicio
 * @author José Manuel Muñoz Simó | irotdev
 * @version v1.0
 */

// Adding AEMETKEY (constant with my personal API key)
// Ask for another one for you here: https://opendata.aemet.es/centrodedescargas/inicio
include('../model/private-api.php');

// Municipality code: https://www.ine.es/daco/daco42/codmun/codmunmapa.htm
CONST MUNICIPALITY = "04075"; // City: Almería --> Pulpí


/**
 * Get with curl twice data from the API of AEMET
 * @param $url
 * @return array
 */
function curlWeather($url): array {
    $curl = curl_init();
    curl_setopt_array($curl, array(
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => "",
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => "GET",
        CURLOPT_HTTPHEADER => array(
            "cache-control: no-cache"
        ),
    ));

    $response = curl_exec($curl);
    $err = curl_error($curl);

    curl_close($curl);
    return array($response, $err);
}


$url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/" . MUNICIPALITY . "/?api_key=" . AEMETKEY;
$callAPI = curlWeather($url);
$response = $callAPI[0];
$err = $callAPI[1];

if ($err) {
    echo "cURL Error #:" . $err;
} else {

    $arr = json_decode($response, true);
    $urlData = utf8_encode($arr["datos"]);
    $callAPI2 = curlWeather($urlData);
    $response2 = $callAPI2[0];
    $err2 = $callAPI2[1];

    if ($err2) {
        echo "cURL Error #:" . $err2;
    } else {
        // AEMET API return the 2nd part of the json stating with [ (which is wrong)
        $json = "{\"data\": " . utf8_encode($response2) . "}";
        $arr2 = json_decode($json, true);

        echo "AEMET API - test";
        echo "Temperature prediction for " . $arr2["data"][0]["nombre"] . ", " . $arr2["data"][0]["provincia"] . " (Spain)<br>";
        $arrDay = $arr2["data"][0]["prediccion"]["dia"];

        echo "Today, day " . date_format(date_create($arrDay[0]["fecha"]), "Y-m-d") . ": <br>";
        echo "-> " . $arrDay[0]["temperatura"]["dato"][0]["value"] . "ºC at " . $arrDay[0]["temperatura"]["dato"][0]["hora"] . "h.<br>";
        echo "-> " . $arrDay[0]["temperatura"]["dato"][1]["value"] . "ºC at " . $arrDay[0]["temperatura"]["dato"][1]["hora"] . "h.<br>";
        echo "-> " . $arrDay[0]["temperatura"]["dato"][2]["value"] . "ºC at " . $arrDay[0]["temperatura"]["dato"][2]["hora"] . "h.<br>";
        echo "-> " . $arrDay[0]["temperatura"]["dato"][3]["value"] . "ºC at " . $arrDay[0]["temperatura"]["dato"][3]["hora"] . "h.<br>";
        echo "<br>";
        echo "Tomorrow, day " . date_format(date_create($arrDay[1]["fecha"]), "Y-m-d") . ": <br>";
        echo "-> " . $arrDay[1]["temperatura"]["dato"][0]["value"] . "ºC at " . $arrDay[1]["temperatura"]["dato"][0]["hora"] . "h.<br>";
        echo "-> " . $arrDay[1]["temperatura"]["dato"][1]["value"] . "ºC at " . $arrDay[1]["temperatura"]["dato"][1]["hora"] . "h.<br>";
        echo "-> " . $arrDay[1]["temperatura"]["dato"][2]["value"] . "ºC at " . $arrDay[1]["temperatura"]["dato"][2]["hora"] . "h.<br>";
        echo "-> " . $arrDay[1]["temperatura"]["dato"][3]["value"] . "ºC at " . $arrDay[1]["temperatura"]["dato"][3]["hora"] . "h.<br>";
    }
}
