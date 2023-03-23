<?php

class FizzBuzz
{
    public const FIZZ = 3;
    public const BUZZ = 5;
    public const MIN = 1;
    public const MAX = 100;


    public function getFizzBuzz()
    {
        for ($i = self::MIN; $i <= self::MAX; $i++) {
            switch ($i) {
                case ($i % 3 === 0 && $i % 5 === 0):
                    echo nl2br("FizzBuzz \n");
                    break;
                case ($i % 3 === 0):
                    echo nl2br("Fizz \n");
                    break;
                case ($i % 5 === 0):
                    echo nl2br("Buzz \n");
                    break;
                default:
                    echo nl2br($i . "\n");
                    break;
            }
        }
    }
}

$fizzbuz = new FizzBuzz();
$fizzbuz->getFizzBuzz();
