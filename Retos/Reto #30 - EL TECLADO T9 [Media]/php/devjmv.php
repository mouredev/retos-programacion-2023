<?php
function tecleando(string $codigo) {
            $teclas   = [
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
            $salida = '';
            $lista = explode('-', $codigo);
            foreach ($lista as $key => $numeros) {
                $tecla = str_split($numeros);
                $salida .= $teclas[$tecla[0]][strlen($numeros)-1];
            }
            return $salida;
        }

        echo tecleando('6-666-88-777-33-3-33-888');
