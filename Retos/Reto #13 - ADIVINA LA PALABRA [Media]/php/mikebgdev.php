<?php

declare(strict_types=1);

use Game as GlobalGame;

class game {
    private $word = '';
    private $secretWord = '';
    private $attempts = 5;
    private $foundWord = false;
    private $foundChars = [];

    public function startGame(): void
    {
        
        $this->word = $this->removeAccents($this->randomWord());
        $this->secretWord = $this->hideChars($this->word);

        while ($this->attempts > 0 && !$this->foundWord)
        {
            echo "Palabra: ". strtoupper($this->secretWord). "\n";
            echo "Ingresa una letra o intenta adivinar la palabra completa ($this->attempts intentos restantes): ";
            $guess = trim(readline());

            if(strlen($guess) === 1) {
                $this->checkLetter($guess);
            } else {
                $this->checkWord($guess);
            }

            if ($this->secretWord == $this->word) {
                $this->foundWord = true;
            }

            echo "\n";
        }

        if ($this->foundWord) {
            echo "¡Felicidades! Has adivinado la palabra \"$this->word\".\n";
        } else {
            echo "Lo siento, no has adivinado la palabra. La palabra era \"$this->word\".\n";
        }
    }

    private function randomWord(): string
    {
        $url = "https://random-word-api.herokuapp.com/word?lang=es";

        $data = file_get_contents($url);
        $jsonData = json_decode($data, true);

        return $jsonData[0] ?? '';
    }

    private function removeAccents ($word): string
    {
        return str_replace(
            array('á', 'é', 'í', 'ó', 'ú', 'ü', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ü'),
            array('a', 'e', 'i', 'o', 'u', 'u', 'A', 'E', 'I', 'O', 'U', 'U'),
            $word
        );
    }

    private function hideChars(string $word): string 
    {
        $charsToHide = (int) round(strlen($word) * 0.6);
        
        $indexToHide = array_rand(str_split($word), $charsToHide);

        foreach ($indexToHide as $index) {
            $word[$index] = "_";
        }

        return $word;
    }

    private function checkLetter(string $guess): void
    {
        if(in_array($guess, $this->foundChars)) {
            echo "Ya has adivinado la letra $guess. Intentalo de nuevo.\n";
        } elseif (strpos($this->word, $guess) !== false) {
            echo "¡Has acertado la letra $guess!\n";
            $this->foundChars[] = $guess;
            $secretWord = str_split($this->secretWord);

            foreach (str_split($this->word) as $index => $letter) {
                if ($letter == $guess) {
                    $secretWord[$index] = $guess;
                }
            }
            $this->secretWord = implode($secretWord);
        }else {
            echo "La letra $guess no se encuentra en la palabra. ¡Inténtalo de nuevo!\n";
            $this->attempts--;
        }
    }

    private function checkWord (string $guess): void
    {
        if (strtolower($guess) == strtolower($this->word)) {
            $this->foundWord = true;
        } else {
            echo "La palabra ingresada no es correcta. ¡Inténtalo de nuevo!\n";
            $this->attempts--;
        }
    }
}

$game = new Game();
$game->startGame();

?>