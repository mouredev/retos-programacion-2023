<?php

class CheckNumber
{
    public $numberEntered;

    public function __construct(int $numberEntered)
    {
        $this->numberEntered = $numberEntered;
    }

    /**
     * It takes a number and checks if it's a Fibonacci number
     * 
     * @param int request_input The number to be checked if it is a Fibonacci number.
     * 
     * @return a string.
     */
    public function IsFibonacci(int $request_input)
    {
        $data     = $request_input;
        $prev_one = 1;
        $prev_two = 0;
        $string = ', no es fibonacci ';
        for ($i = 0; $i <= $data; $i++) {
            $i = ($prev_one + $prev_two);
            $prev_two = $prev_one;
            $prev_one = $i;
            if ($i === $data) {
                $string = ', fibonacci ';
                break;
            }
        }
        return $string;
    }

    /**
     * It checks if a number is prime or not.
     * 
     * @param int request_input The input value to be checked.
     */
    public function IsPrimo(int $request_input)
    {
        $o     = 0;
        $reply = $request_input . ' es primo';
        for ($i = 1; $i <= $request_input; $i++) {
            $op = $request_input % $i === 0 ? $o++ : '';
            if ($op > 1) {
                $reply = $request_input . ' no es primo';
                break;
            }
        }
        return $reply;
    }

    /**
     * > This function takes an integer as input and returns a string that says whether the input is
     * even or odd
     * 
     * @param int request_input The input that the user has sent to the bot.
     * 
     * @return a string.
     */
    public function IsPar(int $request_input)
    {
        $reply = ($request_input % 2 === 0) ? 'y es par.' : 'y es impar.';
        return $reply;
    }

    /**
     * It takes a number, checks if it's prime, fibonacci, or even, and returns a string with the
     * results
     * 
     * @return The output of the methods IsPrimo, IsFibonacci and IsPar.
     */
    public function __toString()
    {
        $data   = $this->numberEntered;
        if (!is_int($data) || $data === 0) {
            throw new Exception("Debe ingresar un valor entero y mayor a 0.");
        }
        $output = $this->IsPrimo($data) . $this->IsFibonacci($data) . $this->IsPar($data);
        return $output;
    }
}

for ($i = 1; $i < 10; $i++) {
    $item = new CheckNumber($i);
    echo $item . "\n";
}
