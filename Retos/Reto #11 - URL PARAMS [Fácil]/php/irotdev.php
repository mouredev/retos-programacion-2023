<?php
/**
 * Reto11 of MoureDev: https://github.com/irotdev/retos-programacion-2023/blob/main/Retos/Reto%20%2311%20-%20URL%20PARAMS%20%5BF%C3%A1cil%5D/ejercicio.md
 * Giving a URL with params, get the value of this params.
 * Example: https://retosdeprogramacion.com?year=2023&challenge=0  --> ["2023", "0"]
 * @author José Manuel Muñoz Simó | irotdev
 * @version v1.0
 */


$url = "https://retosdeprogramacion.com?year=2023&challenge=0";
echo getParamsString($url);

// Others options:
// $currentURL = $_SERVER['REQUEST_SCHEME'] . "://" . $_SERVER['HTTP_HOST'] . ":" . $_SERVER['SERVER_PORT'] . $_SERVER['REQUEST_URI'];
// echo "<br>Params of current URL: " . getParamsString($currentURL);

// For BONUS:
//var_dump(getParamsArray($url));


function getParamsString($url) : String {
    $pos = stripos($url, "?");
    if ($pos) {
        $return = "";
        $stringWithParams = substr($url, $pos+1);
        $arrKeyValueOfParams = explode ("&", $stringWithParams);
        foreach ($arrKeyValueOfParams as $value) {
            $param = substr($value, (strpos($value, "=")+1));
            $return .= "['$param'] ";
        }
        return $return;
    }
    return "There are not params.";
}


// BONUS: Array with keys and values of the params of a URL
function getParamsArray($url) : array {
    $return = array();
    $pos = strpos($url, "?");
    if ($pos) {
        $stringWithParams = substr($url, $pos+1);
        $arrKeyValueOfParams = explode ("&", $stringWithParams);
        foreach ($arrKeyValueOfParams as $value) {
            $arrKeyValueOneParam = explode ("=", $value);
            $return[$arrKeyValueOneParam[0]] = $arrKeyValueOneParam[1];
        }
    }
    return $return;
}



/*
// BONUS: Notes for the future (related with the params)
// If you want to get the current URL, for example:
// http://localhost/PHPLogicProblems/RetosMoureDev/reto11-params.php?example=1&say=Hello
$url = $_SERVER['REQUEST_URI'];     //  /PHPLogicProblems/RetosMoureDev/reto11-params.php?example=1&say=Hello
$url = $_SERVER["SCRIPT_NAME"];     //  /PHPLogicProblems/RetosMoureDev/reto11-params.php
$url = $_SERVER['QUERY_STRING'];    //  example=1&say=Hello
$url = $_SERVER['HTTP_HOST'];       //  localhost
$url = $_SERVER['SERVER_NAME'];     //  localhost
$url = $_SERVER['SERVER_ADDR'];     //  ::1     ((you can change from localhost to 127.0.0.1...))
$url = $_SERVER['PHP_SELF'];        //  /PHPLogicProblems/RetosMoureDev/reto11-params.php
$url = $_SERVER['SCRIPT_FILENAME']; //  C:/xampp/htdocs/PHPLogicProblems/RetosMoureDev/reto11-params.php
$url = $_SERVER['DOCUMENT_ROOT'];   //  C:/xampp/htdocs
$url = $_SERVER['SERVER_PORT'];     //  80
$url = $_SERVER['REQUEST_SCHEME'];  //  http
$url = $_SERVER['SERVER_PROTOCOL']; //  HTTP/1.1

$url = __FILE__;                    //  C:/xampp/htdocs/PHPLogicProblems/RetosMoureDev/reto11-params.php
$url = __DIR__;                     //  C:\xampp\htdocs\PHPLogicProblems\RetosMoureDev

$protocol = ((!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] != 'off') || ($_SERVER['SERVER_PORT'] == 443)) ? "https://" : "http://";   //  http://

// Showing full URL: http://localhost/PHPLogicProblems/RetosMoureDev/reto11-params.php?example=1&say=Hello
$url = $_SERVER['REQUEST_SCHEME'] . "://" . $_SERVER['HTTP_HOST'] . ":" . $_SERVER['SERVER_PORT'] . $_SERVER['REQUEST_URI'];
*/