<?php
/**
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */

class Aurebesh
{
    const CHARS = [
    'A' => 'aurek',
    'B' => 'besh',
    'C' => 'cresh',
    'D' => 'dorn',
    'E' => 'esk',
    'F' => 'forn',
    'G' => 'grek',
    'H' => 'hierba',
    'I' => 'isk',
    'J' => 'jenth',
    'K' => 'krill',
    'L' => 'leth',
    'M' => 'mern',
    'N' => 'nern',
    'O' => 'osk',
    'P' => 'peth',
    'Q' => 'qek',
    'R' => 'resh',
    'S' => 'décimo',
    'T' => 'trino',
    'U' => 'usk',
    'V' => 'vev',
    'W' => 'wesk',
    'X' => 'xesh',
    'Y' => 'yirt',
    'Z' => 'zerek',
    ];

    private $reverse = [];

    public function __construct()
    {
        foreach (self::CHARS as $letter => $v) {
            $this->reverse[$v] = strtolower($letter);
        }
    }

    public function toAurebesh($text): string
    {
        $sentence = "";
        $i = 0;
        while ($i<strlen($text)) {
            $sentence = $sentence . (!empty(self::CHARS[strtoupper($text[$i])])?self::CHARS[strtoupper($text[$i])]:' ');
            $i++;
            //printf("i: %s, sentence: %s\n", $i, $sentence);
        }

        return $sentence;
    }
 
    public function toText($aurebesh): string
    {
        $sentence = "";
        $i = 0;
        $search = "";
        while ($i<strlen($aurebesh)) {
            $search = $search . $aurebesh[$i];
            foreach ($this->reverse as $au => $l) {
                if ($search == $au) {
                    $sentence = $sentence . $l;
                    $search = "";
                    break;
                }
            }
            $i++;
        }

        return $sentence;
    }
}

$test = new Aurebesh();

printf("Traduccion: %s\n", $test->toAurebesh("hola"));
printf("Traduccion: %s\n", $test->toText("hierbaosklethaurek"));
printf("Traduccion: %s\n", $test->toText("hierbaoskleth"));

$answer = readline('¿Quieres jugar (s/n) ');

while ($answer == 's') {
    $word = readline('Pon palabra de español a aurebesh: ');
    if (!empty($word)) {
        printf("La traducción de español a aurebesh de %s es %s\n", $word, $test->toAurebesh($word));
    }
    $word = readline('Pon palabra de aurebesh a español: ');
    if (!empty($word)) {
        printf("La traducción de aurebesh a español de %s es %s\n", $word, $test->toText($word));
    }

    $answer = readline("¿Otra ronda (s/n) ");
}


