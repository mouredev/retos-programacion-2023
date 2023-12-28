<?php

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

 interface IRule {
    public function check(int $number): bool;
    public function getValue(): string;
} 

class FizzRule implements IRule{
    public function check(int $number):bool{
        return $number%3 == 0;
    }

    public function getValue():string{
        return "fizz";
    }
}

class BuzzRule implements IRule{
    public function check(int $number):bool{
        return $number%5 == 0;
    }

    public function getValue():string{
        return "buzz";
    }
}

// Clase principal que genera y muestra los resultados de FizzBuzz
class FizzBuzz {
    private $rules = [];


    public function __construct(array $rules) {
        $this->rules = $rules;
    }

    public function generate(int $n): array {
        $result = [];
        for ($i = 1; $i <= $n; $i++) {
            $value = '';
            foreach ($this->rules as $rule) {
                if ($rule->check($i)) {
                    $value .= $rule->getValue();
                }
            }
            
            $result[] = ($value !== '') ? $value : (string)$i;
        }
        return $result;
    }

    // Muestra los resultados en la consola
    public function printResult(int $n): void {
        $result = $this->generate($n);
        foreach ($result as $item) {
            echo $item . "\n";
        }
    }
}


echo "Reto #0: EL FAMOSO \"FIZZ BUZZ\"\n";
$fizzBuzz = new FizzBuzz([new FizzRule(), new BuzzRule()]);
$fizzBuzz->printResult(100);

?>