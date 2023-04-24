<?php

interface SistemaInterface
{
    public function convertir($numero): string;
}

class SistemaOctal implements SistemaInterface
{
    public function convertir($numero): string
    {
        $resto = $numero % 8;
        $numero = intdiv($numero, 8);
        if($numero < 8){
            return intval($numero.$resto);
        }else{
            return $this->convertir($numero).$resto;
        }
    }
}

class SistemaHexadecimal implements SistemaInterface
{
    public function convertir($numero): string
    {
        $resto = $numero % 16;
        $numero = intdiv($numero, 16);
        if($numero < 16){
            return $this->evaluate($numero).$this->evaluate($resto);
        }else{
            return $this->convertir($numero).$this->evaluate($resto);
        }
    }

    private function evaluate($number)
    {
        if($number > 9){
            return chr($number + 55);
        }
        return $number;
    }
}

class Convertir
{
    private $sistemaInterface;

    function __construct(SistemaInterface $sistemaInterface)
    {
        $this->sistemaInterface = $sistemaInterface;
    }

    public function convertir($number)
    {
        return $this->sistemaInterface->convertir($number);
    }
}

echo "<form method='post' action=''>
    <input type='text' placeholder='number' name='txtNumber' />
    <button type='submit' name='btnCalculateOctal'>Calcular Octal</button>
    <button type='submit' name='btnCalculateHexadecimal'>Calcular Hexadecimal</button>
</form>";

if(isset($_POST['btnCalculateOctal'])){

    if($_POST['txtNumber']){
        
        $convertir = new Convertir(new SistemaOctal);
        echo $_POST['txtNumber']." en base octal: ".$convertir->convertir($_POST['txtNumber']);
    }
}

if(isset($_POST['btnCalculateHexadecimal'])){

    if($_POST['txtNumber']){
        
        $convertir = new Convertir(new SistemaHexadecimal);
        echo $_POST['txtNumber']." en base hexadecimal: ".$convertir->convertir($_POST['txtNumber']);
    }
}
