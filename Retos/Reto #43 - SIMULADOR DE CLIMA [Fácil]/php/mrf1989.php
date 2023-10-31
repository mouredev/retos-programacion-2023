<?php

function predecir_clima(int $dias, int $tmp_inicial, int $p_lluvia_inicial): void
{
    $tmp = $tmp_inicial;
    $p_lluvia = $p_lluvia_inicial;
    $dias_lluviosos = 0;
    $tmp_diarias = array($tmp_inicial);

    for ($i = 1; $i <= $dias; $i++) {
        echo "Día {$i}\n";
        echo "La probabilidad de lluvia es del {$p_lluvia}%\n";

        $cambio = rand(0, 100);

        if ($cambio <= 10) {
            $subida = rand(0, 1);

            if ($subida) {
                $tmp += 2;
            } else {
                $tmp -= 2;
            }
        }

        echo "La temperatura es de {$tmp} grados.\n";
        array_push($tmp_diarias, $tmp);

        if ($p_lluvia == 100) {
            $dias_lluviosos++;
        }


        if ($tmp > 25) {
            $p_lluvia += 20;
            if ($p_lluvia > 100) {
                $p_lluvia = 100;
                $tmp -= 1;
            }
        } else if ($tmp < 5) {
            $p_lluvia -= 20;
            if ($p_lluvia < 0) {
                $p_lluvia = 0;
            }
        }
    }

    echo "RESUMEN:\n";
    echo "- Días lluviosos: {$dias_lluviosos}.\n";
    echo "Temperatura máxima: " . max($tmp_diarias) . " grados.\n";
    echo "Tempratura mínima: " . min($tmp_diarias) . " grados.\n";
}

predecir_clima(24, 24, 20);
