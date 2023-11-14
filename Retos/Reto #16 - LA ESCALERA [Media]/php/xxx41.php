<?php

function buildSteps($steps): void
{
    if ($steps == 0) {
        print('__' . PHP_EOL);
        return;
    };

    $output = '';
    $repetitionsRange = $steps > 0 ? range($steps * 2, 0, 2) : range(0, abs($steps) * 2, 2);
    foreach ($repetitionsRange as $index => $repetitions) {
        $repeatWhitespaces = $steps > 0 ? $repetitions : $repetitions - 1;
        $repeatWhitespaces = $steps < 0 && $index === 0 ? 0 : abs($repeatWhitespaces);
        $finalChars = $steps > 0 ? '_|' : '|_';
        $finalChars = $index === 0 ? '_' : $finalChars;
        $output .= str_repeat(' ', $repeatWhitespaces) . $finalChars . PHP_EOL;
    }

    print($output . PHP_EOL);
}

buildSteps(0);
buildSteps(5);
buildSteps(-5);
