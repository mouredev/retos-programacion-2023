<?php

class HackerLanguage
{

    private const Dictionary = [
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

    public $text;

    public function __construct(string $text)
    {
        $this->text = $text;
    }

    /**
     * It takes the text, converts it to lowercase, splits it into an array, then loops through the
     * array and checks if the value is in the dictionary. If it is, it adds the value to the
     * textConverted variable
     * 
     * @return string The method is returning the converted text.
     */
    public function conversionDictionary()
    {
        $lowerCase     = strtolower( $this->text );

        $textToConvert = str_split( $lowerCase );
        
        $dictionary    = self::Dictionary;
        
        $textConverted = '';
        
        foreach ( $dictionary as $key => $value ) {
            if ( in_array( $key, $textToConvert ) ) {
                $textConverted .= $value;
            }
        }

        return $textConverted;
    }

    public function __toString()
    {

        $retornedOutput = $this->conversionDictionary();

        return $retornedOutput;
    }
}

$reto1 = new HackerLanguage('Demo de reto');

echo $reto1;
