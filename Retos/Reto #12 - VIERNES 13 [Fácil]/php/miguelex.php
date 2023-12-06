<?php

    function isFridaythe13th($month, $year) {

        $dayOfWeek = date('N', strtotime("$year-$month-13"));
        return $dayOfWeek= 5;
    }

    $isFriday = isFridaythe13th(10, 2023) ? 'True' : 'False';
    echo "¿Hay viernes 13 en octubre de 2023? $isFriday\n";

    $isFriday = isFridaythe13th(3, 2023) ? 'True' : 'False';
    echo "¿Hay viernes 13 en marzo de 2023? $isFriday\n";

?>