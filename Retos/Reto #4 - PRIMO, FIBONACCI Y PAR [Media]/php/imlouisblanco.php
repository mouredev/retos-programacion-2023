<?php

class CustomValidation
{
    protected $number;

    public function __construct(int $number)
    {
        $this->number = $number;
    }

    public function getValidation(): string
    {
        if (!$this->isValidInput()) {
            return 'el número ingresado no es válido';
        }

        $translations = [
            $this->isPrime() ? 'es primo' : 'no es primo',
            $this->isFibonacci() ? 'es fibonacci' : 'no es fibonacci',
            $this->isEven() ? 'es par' : 'no es par',
        ];

        return sprintf("%s, %s y %s", $translations[0], $translations[1], $translations[2]);
    }

    protected function isValidInput(): bool
    {
        //I decided to accept only natural numbers
        return $this->number >= 1;
    }

    protected function isFibonacci(): bool
    {
        if ($this->number < 4) {
            return true;
        }

        return in_array($this->number, $this->getFibonacciNumbers());
    }

    private function getFibonacciNumbers(): array
    {
        $fibonacci = [0, 1];

        while ($fibonacci[count($fibonacci) - 1] <  $this->number) {
            $newPosition = $fibonacci[count($fibonacci) - 1] + $fibonacci[count($fibonacci) - 2];

            $fibonacci[] = $newPosition;
        }

        return $fibonacci;
    }

    protected function isPrime(): bool
    {
        if ($this->number == 1) {
            return false;
        }

        if ($this->number == 2) {
            return true;
        }

        for ($i = 2; $i < $this->number; $i++) {
            if ($this->number % $i == 0) {
                return false;
            }
        }

        return true;
    }

    protected function isEven(): bool
    {
        return $this->number % 2 == 0;
    }
}

// Example:
$numbers = [0,1,6,13,14,19];
foreach ($numbers as $number) {
    $customValidation = new CustomValidation($number);

    echo $customValidation->getValidation(). "\n";
}

/* Results:
0 - el número ingresado no es válido
1 - no es primo, es fibonacci y no es par
6 - no es primo, no es fibonacci y es par
13 - es primo, es fibonacci y no es par
14 - no es primo, no es fibonacci y es par
19 - es primo, no es fibonacci y no es par
*/
