<?php

/**
 * Write a program that displays by console (with a print) the numbers 1 to 100 (both included 
 * and with a line break between each print), substituting the following:
 * - Multiples of 3 for the word "fizz".
 * - Multiples of 5 for the word "buzz".
 * - Multiples of 3 and 5 at the same time for the word "fizzbuzz".
 * 
 */
class reto0
{
    private const MIN = 1;
    private const MAX = 100;
    private const CONDITIONS = [
        [3, 'fizz'],
        [5, 'buzz'],
    ];

    public function run()
    {
        echo join(PHP_EOL, $this->generateData()).PHP_EOL;
    }

    /**
     * Generate an array with data between $min and $max
     * 
     * @param int $min
     * @param int $max
     * @return array
     */
    private function generateData(int $min = self::MIN, int $max = self::MAX): array
    {
        $result = [];

        for ($i = $min; $i <= $max; $i++)
        {
            $text = $this->getReplacingStringIfConditions($i);
            $result[] = $text ?: $i;
        }

        return $result;
    }

    /**
     * Check the $number with each $condition and concatenate the replacing strings
     * 
     * @param int $number the number to check
     * @param array $conditions an array of [$factor, $string]
     * @return string
     */
    private function getReplacingStringIfConditions(int $number, array $conditions = self::CONDITIONS): string
    {
        $result = '';

        foreach($conditions as $condition)
        {
            list($factor, $string) = $condition;
            $result .= ($this->isMultipleOf($number, $factor)) ? $string : '';
        }

        return $result;
    }

    /**
     * Check if $number is multiple of $factor
     * 
     * @param int $number
     * @param int $factor
     * @return bool
     */
    private function isMultipleOf(int $number, int $factor): bool
    {
        return $number % $factor === 0;
    }
}

(new reto0())->run();