<?php

class FizzBuzz
{
    private $maximo;

    public function __construct(int $maximo)
    {
        $this->maximo = $maximo;
    }

    public function pintar()
    {
        for($i = 1; $i<= $this->maximo; $i++) {
            echo $this->transformar($i) . "\n";
        }
    }

    private function transformar(int $numero): string
    {
        if ($numero % 5 === 0 && $numero % 3 === 0) {
            return 'fizzbuzz';
        }
        if ($numero % 3 === 0) {
            return 'fizz';
        }
        if ($numero % 5 === 0 && $numero % 3 === 0) {
            return 'buzz';
        }
        return (string)$numero;
    }

}

$fizz = new FizzBuzz(100);
$fizz->pintar();