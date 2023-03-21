<?php

/*
 * Función para, según el mes y año que se le indique, devolverá si este tiene viernes 13 o no. 
 */

function fridaythe13rd($month, $year)
{
    $date = strtotime("$year-$month-13"); // formateo fecha en año-mes-día
    if (date('N', $date) == 5) { // si es 5, significa que se trata de un viernes, ya que la semana en PHP empieza en lunes (1)
        echo "El mes de $month del año $year contiene un Viernes 13";
    } else {
        echo "El mes de $month del año $year NO contiene un Viernes 13";
    }
}

echo '<pre>Ejemplo de mes 02 de 2023</pre>';
fridaythe13rd(2, 2023);
echo '<pre>Ejemplo de mes 09 de 2023</pre>';
fridaythe13rd(10, 2023);
