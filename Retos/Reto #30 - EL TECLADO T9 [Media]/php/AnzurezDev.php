<?php
    function t9_message($string) { 
        $chars   = [
            [" "],
            [",", ".", "?", "!"],
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"],
            ["J", "K", "L"],
            ["M", "N", "O"],
            ["P", "Q", "R", "S"],
            ["T", "U", "V"],
            ["W", "X", "Y", "Z"]
        ];
        $message = "";
        $elements= explode("-", $string);

        foreach ($elements as $element) {
            $keys       = str_split($element);
            $cursor     = -1;
            $position   = 0;

            foreach ($keys as $key) {
                $position = $key;
                $cursor++;
            }

            $message .= $chars[$position][$cursor];
        }

        return $message;
    }

echo t9_message("6-666-88-777-33-3-33-888") . "\n";
echo t9_message("6-2-777-222-666-7777") . "\n";