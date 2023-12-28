<?php
/*
    Para ejecutarlo revisar el repositorio:
    https://github.com/EjemplosADSI/konami-code
*/
require "vendor\autoload.php";

use Zenithies\Toolkit\ReadKey\Interceptor;

$key_position = 0;
$KONAMI_CODE = [
    Interceptor::KEY_UP, Interceptor::KEY_UP, Interceptor::KEY_DOWN,
    Interceptor::KEY_DOWN, Interceptor::KEY_LEFT, Interceptor::KEY_RIGHT,
    Interceptor::KEY_LEFT, Interceptor::KEY_RIGHT, 98, 97,
];
$ICONS = [
    Interceptor::KEY_UP => "", Interceptor::KEY_DOWN => "",
    Interceptor::KEY_LEFT => "", Interceptor::KEY_RIGHT => "",
    98 => "b", 97 => "a",
];

$keys = Interceptor::I();
echo "\033[31m\e[1mKonami Code \e[32m presione q para salir \n";

if ($keys->init()) {
    while (true) {
        $key = $keys->intercept();
        if (in_array($key, [113, 81])) {
            Interceptor::eprintln("\e[7;34;40mSalida registrada\e[0m");
            exit(0);
        }
        if (!on_press($key)) {
            exit(0);
        }
    }
}

function on_press($key)
{
    global $key_position, $last_key, $KONAMI_CODE, $ICONS;
    echo (in_array($key, $KONAMI_CODE)) ? "$ICONS[$key]" : chr($key);
    if ($key == $KONAMI_CODE[$key_position]) {
        $key_position += 1;
    } elseif ($key == $KONAMI_CODE[0]) {
        $key_position = ($last_key == $KONAMI_CODE[0]) ? 2 : 1;
    } else {
        $key_position = 0;
    }

    if ($key_position == count($KONAMI_CODE)) {
        echo "\n\e[39m";
        echo "\e[41m╦╔═╔═╗╔╗╔╔═╗╔╦╗╦  ╔═╗╔═╗╔╦╗╔═╗\n";
        echo "\e[41m╠╩╗║ ║║║║╠═╣║║║║  ║  ║ ║ ║║║╣ \n";
        echo "\e[41m╩ ╩╚═╝╝╚╝╩ ╩╩ ╩╩  ╚═╝╚═╝═╩╝╚═╝\n";
        echo "\e[0m";
        return false;
    }
    $last_key = $key;
    return true;
}
