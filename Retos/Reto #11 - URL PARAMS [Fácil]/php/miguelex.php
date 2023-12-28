<?php
    function FindParameters($cadena){

        $params = array();
        
        $urlDividida = explode("?", $cadena);

        if (count($urlDividida) > 1){
            $parametros = explode("&", $urlDividida[1]);
            
            foreach ($parametros as $parametro){
                $parametroDividido = explode("=", $parametro);
                if($parametroDividido[1] != ""){
                    array_push($params, strval($parametroDividido[1]));
                }
            }

            if (count($params) > 0){
                echo "[";
                foreach ($params as $index => $param) {
                    echo '"'. $param . '"';
                    if ($index < count($params) - 1) {
                        echo ", ";
                    }
                }
                echo "]\n";
            } else {
                echo "La Url no tiene parametros\n";
            }                      
        } else {
            echo "La Url no tiene parametros\n";
        }
    }
    @FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0");
    @FindParameters("https://retosdeprogramacion.com");
    @FindParameters("https://retosdeprogramacion.com?");
    @FindParameters("https://retosdeprogramacion.com?year=2023");
    @FindParameters("https://retosdeprogramacion.com?year=2023&");
    @FindParameters("https://retosdeprogramacion.com?year=&");
    @FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python");
?>