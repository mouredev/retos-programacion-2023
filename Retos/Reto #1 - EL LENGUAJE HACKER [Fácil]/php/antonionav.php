<?php

/*
 * Write a program that receives a text and transforms natural language to.
 * "hacker language" (actually known as "leet" or "1337"). This language
 * is characterized by substituting alphanumeric characters.
 * - Use this table (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 * with the alphabet and numbers in "leet".
 * (Use the first option of each transformation, for example "4" for "a")
 */
 class reto1
{
    private const LEET_DICTIONARY = [
        'a' => '4',
        'á' => '4',
        'ä' => '4',
        'à' => '4',
        'â' => '4',
        'b' => 'I3',
        'c' => '[',
        'd' => ')',
        'e' => '3',
        'é' => '3',
        'ë' => '3',
        'è' => '3',
        'ê' => '3',
        'f' => '|=',
        'g' => '&',
        'h' => '#',
        'i' => '1',
        'í' => '1',
        'ï' => '1',
        'ì' => '1',
        'î' => '1',
        'j' => ',_|',
        'k' => '>|',
        'l' => '1',
        'm' => '/\\/\\',
        'n' => '^/',
        'ñ' => '^/',
        'o' => '0',
        'ó' => '0',
        'ö' => '0',
        'ò' => '0',
        'ô' => '0',
        'p' => '|*',
        'q' => '(_,)',
        'r' => 'I2',
        's' => '5',
        't' => '7',
        'u' => '(_)',
        'ú' => '(_)',
        'ü' => '(_)',
        'ù' => '(_)',
        'û' => '(_)',
        'v' => '\\/',
        'w' => '\\/\\/',
        'x' => '><',
        'y' => 'j',
        'z' => '2',
        '0' => 'o',
        '1' => 'L',
        '2' => 'R',
        '3' => 'E',
        '4' => 'A',
        '5' => 'S',
        '6' => 'b',
        '7' => 'T',
        '8' => 'B',
        '9' => 'g'
    ];

    public function run(array $argv)
    {
        if (!$this->validateParams($argv))
        {
            $this->printHelp();
            exit(0);
        }

        $this->displayText($this->transformText($argv[1]));
    }

    /**
     * Help text to show the usage.
     */
    private function printHelp(): void
    {
        echo PHP_EOL.'Usage: php antonionav.php "text to transform".'.PHP_EOL;
        echo '       Do not start your text with "-"'.PHP_EOL;
    }

    /**
     * A minimum validation for the parameters received
     * 
     * @param array $argv A collection with all command line parameters.
     * @return bool
     */
    private function validateParams(array $argv): bool
    {
        $valid = true;
        $numParams = count($argv);

        if (($numParams === 1) ||
            ($numParams > 2) ||
            (($numParams === 2) && (substr($argv[1], 0, 1) === '-'))
        ) {
            $valid = false;
        }

        return $valid;
    }

    /**
     * Replace the $text given with the DICTIONARY
     * 
     * @param string $text to replace
     * @param array $dictionary a collection with 'character' => 'replacement'.
     * @return string
     */
    private function transformText(string $text, array $dictionary = self::LEET_DICTIONARY): string
    {
        return strtr(strtolower($text), $dictionary);
    }

    /**
     * Print to std out the $text given
     * 
     * @param string $text
     * @return void
     */
    private function displayText(string $text): void
    {
        echo PHP_EOL.'"'.$text.'"'.PHP_EOL.PHP_EOL;
    }

}

(new reto1())->run($argv);