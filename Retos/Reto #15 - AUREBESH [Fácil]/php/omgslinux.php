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
    const CHARS2 = [
        'ae' => "enth",
        'ch' => 'cherek',
        'eo' => 'onith',
        'kh' => 'krenth',
        'ng' => 'nen',
        'oo' => 'orenth',
        'sh' => 'shen',
        'th' => 'thesh'
    ];

    private $_reverse = [];
    private $_reverse2 = [];

    public function __construct()
    {
        foreach (self::CHARS as $letter => $v) {
            $this->_reverse[$v] = strtolower($letter);
        }
        foreach (self::CHARS2 as $letter => $v) {
            $this->_reverse2[$v] = strtolower($letter);
        }
    }

    public function toAurebesh($text): string
    {
        $sentence = "";
        $i = 0;
        while ($i<strlen($text)) {
            $double = ($i+1<strlen($text)?strtolower($text[$i] . $text[$i+1]):null);
            if (null != $double && !empty(self::CHARS2[$double])) {
                $sentence = $sentence . self::CHARS2[$double];
                $i++;
                //printf("double: %s, sentence: %s\n", $double, $sentence);

            } else {
                $sentence = $sentence . (!empty(self::CHARS[strtoupper($text[$i])])?self::CHARS[strtoupper($text[$i])]:$text[$i]);
                //printf("i: %s, sentence: %s\n", $i, $sentence);
            }
            $i++;
        }

        return $sentence;
    }
 
    public function toText($aurebesh): string
    {
        $sentence = $search = "";
        $i = 0;
        while ($i<strlen($aurebesh)) {
            $found = null;
            $search = $search . $aurebesh[$i];
            foreach ($this->_reverse2 as $au => $l) {
                if (strtolower($search) == $au) {
                    $found = $l;
                }
            }
            foreach ($this->_reverse as $au => $l) {
                if (strtolower($search) == $au) {
                    $found = strtolower($l);
                }
            }
            if ($found) {
                $sentence = $sentence . $found;
                //printf("Se encontro parcial %s, total %s\n", $search, $sentence);
                $search = "";
            } else {
                // Comprobamos que sea un caracter
                if (strlen($search)==1) {
                    $s=ord(strtoupper($search));
                    if ($s<ord('A') || $s>ord('Z')) {
                        // No es un caracter conocido, por lo que lo añadimos
                        $sentence = $sentence . $search;
                        //printf("NO Se encontro parcial %s, total %s\n", $search, $sentence);
                        $search = "";
                    }
                }
            }
            $i++;
        }

        return $sentence;
    }
}

$test = new Aurebesh();

printf("Traduccion: %s\n", $test->toAurebesh("hola, paella"));
printf("Traduccion: %s\n", $test->toText("hola, paella"));

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


