<?php

$col = "CA";
getColumnNumber($col);

function getColumnNumber ($column){
    $callback = function ($acc, $cur) {
            $acc['total'] = (ord($cur) - 64) * pow(26, $acc['key']) + $acc['total'];
            $acc['key'] = $acc['key'] + 1;
            return $acc;
    };

    if ($column != null && !preg_match('/[^A-Z]/', $column)) {
        $columNumber = array_reduce(array_reverse(str_split($column)), $callback, ['key' => 0, 'total' => 0])['total'];
        echo "Result: $columNumber";
     } else {
        echo "Invalid column";
    }
}

?>