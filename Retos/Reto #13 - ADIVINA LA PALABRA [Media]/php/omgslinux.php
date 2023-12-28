#!/usr/bin/php
<?php

/**
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

class WordGuesser
{
    const URL="https://random-word-api.herokuapp.com/word?lang=es";
    private $tries;
    private $word=null;
    private $guessed='';
    private $minLength = 7;
    private $maxtries;

    public function checkInput($input)
    {
        if ($input!=$this->word) {
            $charnum = 0;
            while ($charnum < strlen($input)) {
                $pos=0;
                while ($pos < strlen($this->guessed)) {
                    if ($this->word[$pos]==$input[$charnum]) {
                        $this->guessed[$pos]=$input[$charnum];
                    }
                    $pos++;
                }
                $charnum++;
                $this->tries++;
            }

        } else {
            $this->tries++;
            $this->guessed = $this->word;
        }
    }

    public function getInput()
    {
        $remain = $this->maxtries - $this->tries;
        return "Palabra: ".$this->getGuessed()." Llevas ".$this->tries." intentos, quedan ".$remain.". Pon palabra o letra ";
    }

    public function getGuessed(): string
    {
        return $this->guessed;
    }

    public function getMinLength(): int
    {
        return $this->minLength;
    }

    public function setMinLength(int $int)
    {
        if ($int > 0) {
            $this->minLength = $int;
        }
    }

    public function getResults(): string
    {
        if ($this->isFinished()) {
            $winner=$this->getGuessed()==$this->word;
            $resultText="";
            if (!$winner) {
                $resultText="Lástima, perdiste. La palabra era ". $this->word;
            } else {
                $resultText="¡¡¡Enhorabuena, adivinaste la palabra (". $this->word.") en ". $this->tries." intentos!!!";
            }
        } else {
            $resultText="¡¡La partida no ha terminado!!";
        }

        return $resultText;
    }

    public function init(): bool
    {
        $word = null;
        while (strlen($word) < $this->minLength) {
            $word = $this->requestWord();
            //print($word);
        }

        $this->word = $this->guessed = strtolower($word);
        $this->maxtries = strlen($word) +5;

        // Vamos a ocultar hasta el 60% de las letras
        $hidden = 0;
        while ($hidden < (strlen($word) * 0.6)) {
            $pos = rand(1, strlen(($word)))-1;

            if ($this->guessed[$pos] != '_') {
                $this->guessed[$pos] = '_';
                $hidden++;
            }
        }
        $this->tries = 0;

        return strlen($word)>=$this->minLength;
    }

    public function isFinished(): bool
    {
        if ($this->tries>=$this->maxtries) {
            return true;
        }

        if ($this->guessed === $this->word) {
            return true;
        }

        return false;
    }

    public function isWinner(): bool
    {
        if ($this->isFinished()) {
            return $this->maxtries>$this->tries;
        }

        return false;
    }

    public function requestWord(): string
    {
        $result = null;
        while (null == $result) {
            $result = json_decode($this->request(self::URL), true);
            // Evitar que haya algún espacio en la palabra
            if (stripos($result[0], ' ')) {
                $result = null;
            }
        }
        $search = ['á', 'é', 'í', 'ó', 'ú'];
        $replace = ['a', 'e', 'i', 'o', 'u'];
        $word = (str_replace($search, $replace, $result[0]));
        
        return $word;
    }

    private function request(string $url, string $method = 'GET'): string
    {
        $contents = file_get_contents(
            $url, false, stream_context_create(
                [
                'http' => [
                'method' => $method,
                'header' => 'Content-type: application/json',
                ],
                ]
            )
        );
        //print(__LINE__ . ":" . $contents . "\n");
        return $contents;
    }
}

$game = new WordGuesser();

$answer = readline('¿Quieres jugar (s/n) ');
$total = $wins = 0;
while ($answer == 's') {
    $value = readline('Pon longitud mínima de la palabra: ('.$game->getMinLength().') ');
    if (!empty($value)) {
        $game->setMinLength(intval($value));
    }
    $game->init();
    $total++;
    while (!$game->isFinished()) {
        $answer = readline("Partida $total. " . $game->getInput());
        $game->checkInput($answer);
    }
    if ($game->isWinner()) {
        $wins++;
    }
    print($game->getResults() . "\n\n");
    print("Balance: $total partidas, $wins victorias.\n");
    $answer = readline("¿Otra partida (s/n) ");
}

print("¡¡Hasta la próxima!!\n");
