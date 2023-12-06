<?php

declare (strict_types = 1);

class Game
{
    private string $word;
    private array $hiddenLetters;
    private string $hiddenWord;
    private int $lives = 5;

    /**
     * The function "clean" clears the console screen in PHP, using different commands depending on the
     * operating system.
     */
    private function clean(): void
    {
        if (str_starts_with(strtolower(PHP_OS), 'win')) {
            system('cls');
        } else {
            system('clear');
        }
    }

    /**
     * The function "hideWord" takes a string as input, randomly selects a number of letters to hide,
     * replaces those letters with underscores, and stores the original word and the hidden word.
     *
     * @param string word The `word` parameter is a string that represents the word that needs to be
     * hidden.
     */
    private function hideWord(string $word): void
    {
        $this->word = $word;
        $wordArray = str_split($word);
        $totalLetters = count($wordArray);
        $maxHiddenLetters = intval($totalLetters * 0.6);

        $totalHiddenLetters = rand(1, $maxHiddenLetters);

        for ($i = 0; $i < $totalHiddenLetters; $i++) {
            $indexLetter = rand(0, $totalLetters - 1);
            $this->hiddenLetters[$wordArray[$indexLetter]] = $indexLetter;
            $wordArray[$indexLetter] = '_';
        }

        $this->hiddenWord = implode($wordArray);
    }

    /**
     * The function starts a game where the user guesses letters to uncover a hidden word, with a
     * limited number of lives.
     *
     * @param string word The "word" parameter is a string that represents the word that needs to be
     * guessed in a game.
     */
    public function start(string $word): void
    {
        $this->hideWord($word);

        while ($this->hiddenWord !== $this->word && $this->lives > 0) {
            $this->clean();
            echo "Remaining lives: $this->lives", PHP_EOL;
            echo $this->hiddenWord, PHP_EOL;
            $choose = readline('Choose a letter: ');

            if (array_key_exists($choose, $this->hiddenLetters)) {
                $this->hiddenWord[$this->hiddenLetters[$choose]] = $choose;
                unset($this->hiddenLetters[$choose]);
            } else {
                $this->lives--;
            }
        }

        if ($this->hiddenWord === $this->word) {
            echo "Congratulations! The hidden word was $this->word";
        } elseif ($this->lives === 0) {
            echo "You lost. The hidden word was $this->word";
        }
    }
}

$game = new Game();
$game->start('crocodile');
