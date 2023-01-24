<?php
class PasswordGenerator
{

    private const Conditional = array(
        'abcdefghijklmnopqrstvxyz',
        'ABCDEFGHIKLMNOPQRSTVXYZ',
        '0123456789',
        '|,@#~$%()=^*+[]{}-_<>+&',
    );

    private const MinLimit = 8;

    private const MaxLimit = 16;

    public $combination;

    public function __construct(string $combination)
    {
        $this->combination = $combination;
    }

    /**
     * It generates a random password based on the combination of characters you want to use
     * 
     * @return A string with a random password.
     */
    public function generatedRandomPassword()
    {
        $parameters = $this->combination;
        if (!is_int($parameters) && $parameters > 4) {
            throw new Exception("Debe ingresar un valor entero y que sea menor o igual 4.");
        }
        $rules  = $this->getStringCharacters($parameters);
        $limit  = rand(self::MinLimit, self::MaxLimit);
        $string = substr(str_shuffle($rules), 0, $limit);
        return $string;
    }

    /**
     * It takes an integer as an argument and returns a string of characters based on the integer value
     * 
     * @param int ps_option This is the option you want to use.
     * 
     * @return The string of characters that are used to create the password.
     */
    public function getStringCharacters(int $ps_option)
    {
        $option            = $ps_option - 1;
        $combination_rules = self::Conditional;
        $string_values     = '';
        for ($i = 0; $i <= count($combination_rules); $i++) {
            $string_values .= self::Conditional[$i];
            if ($i == ($option)) {
                break;
            }
        }
        return $string_values;
    }

    public function __toString()
    {
        $output = $this->generatedRandomPassword();
        return $output;
    }
}

// 1 Letras minusculas
// 2 Letras Mayusculas
// 3 Con numeros
// 4 Con symbols
$newClass = array(
    new PasswordGenerator(1),
    new PasswordGenerator(2),
    new PasswordGenerator(3),
    new PasswordGenerator(4)
);
foreach($newClass as $output){
    echo $output . "\n";
}

