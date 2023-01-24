<?php

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 *
 * Version: PHP 8.2
 */

class RangePassword
{
    protected int $max;
    protected int $min;

    public function __construct($max, $min)
    {
        $this->max = $max;
        $this->min = $min;
    }

    public function getMax():int
    {
        return $this->max;
    }
    public function getMin():int
    {
        return $this->min;
    }
}

class Password
{
    /** @var RangePassword[] $ranges */
    protected array $ranges = [];
    protected int $length = 8;

    public function __invoke($length = 8, $capitalLetters = false, $numbers = false, $symbols = false)
    {
        $this->setLength($length);
        if($capitalLetters){
            $this->setCapitalLetters();
        }
        if($numbers) {
            $this->setNumbers();
        }
        if($symbols){
            $this->setSymbols();
        }
        return $this->build();
    }
    public function __construct()
    {
        $this->ranges[] = new RangePassword(97, 122);
    }

    public function setLength(int $length):Password
    {
        $this->length = $length;
        return $this;
    }

    public function setCapitalLetters():Password
    {
        $this->ranges[] = new RangePassword(65, 90);
        return $this;
    }
    public function setNumbers():Password
    {
        $this->ranges[] = new RangePassword(48, 57);
        return $this;
    }

    public function setSymbols():Password
    {
        $this->ranges[] = new RangePassword(33, 47);
        $this->ranges[] = new RangePassword(58, 64);
        $this->ranges[] = new RangePassword(91, 95);
        $this->ranges[] = new RangePassword(123, 126);
        return $this;
    }


    public function build():string
    {
        $keyFirst = 0;
        $keyLast = count($this->ranges) - 1;
        $character = 0;
        $password = "";
        while($this->length > $character){
            $randomKey = rand($keyFirst, $keyLast);
            $range = $this->ranges[$randomKey];
            $randomNumber = rand($range->getMin(), $range->getMax());
            $password .= chr($randomNumber);
            $character++;
        }
        return $password;
    }
}
$password = new Password;
$password = $password(9, true, true, false);
echo "$password \n";
