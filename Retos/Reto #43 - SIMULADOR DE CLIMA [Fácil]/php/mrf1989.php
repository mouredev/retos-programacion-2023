<?php

function predecir_clima(int $dias, int $tmp_inicial, int $p_lluvia_inicial): void
{
    $tmp = $tmp_inicial;
    $p_lluvia = $p_lluvia_inicial;
    $dias_lluviosos = 0;
    $tmp_diarias = array($tmp_inicial);

    echo "Hace {$tmp} grados actualmente, con {$p_lluvia}% de probabilidad de lluvia.\n";
    echo "Predicciones para los {$dias} días siguientes:\n\n";

    for ($i = 1; $i <= $dias; $i++) {
        echo "- Día {$i}\n";
        echo "La probabilidad de lluvia es del {$p_lluvia}%\n";

        $random = rand(0, 100);

        if ($random <= 10) {
            $subida = rand(0, 1);

            if ($subida) {
                $tmp += 2;
            } else {
                $tmp -= 2;
            }
        }

        echo "La temperatura es de {$tmp} grados.\n";
        array_push($tmp_diarias, $tmp);

        if ($random <= $p_lluvia) {
            echo "Es una jornada de lluvias.\n";
            $tmp -= 1;
            $dias_lluviosos++;
        }

        echo "\n";

        if ($tmp > 25) {
            $p_lluvia += 20;
            if ($p_lluvia > 100) {
                $p_lluvia = 100;
            }
        } else if ($tmp < 5) {
            $p_lluvia -= 20;
            if ($p_lluvia < 0) {
                $p_lluvia = 0;
            }
        }
    }

    echo "RESUMEN:\n";
    echo "- Temperatura máxima: " . max($tmp_diarias) . " grados.\n";
    echo "- Tempratura mínima: " . min($tmp_diarias) . " grados.\n";
    echo "- Días lluviosos: {$dias_lluviosos}.\n";
}

predecir_clima(10, 24, 30);
