<?php 

class Pfe {
    public int $number;
    private string $message;
    static bool $isPrime = false;
    static bool $isEven = false;
    static bool $isFibo = false;

    public function __construct(int $number){
        $this->number = $number;
        try {
            
            if ($number < 0) {
                throw new TypeError("The number must be greater than 0 😠 "); 
            }
            if (!is_int($number)) {
                throw new TypeError("The variable must be a number 😠 you type: ". gettype($number)); 
            }
            $this->number = $number;
        } catch (\Throwable  $e) {
           exit($e);
        }
    }

    private function isPrime():bool{
        $i = 1;
        $count = 0;
        while ($i <= $this->number) {
            if ($count > 2) {
                break;
            }

            if ($this->number % $i == 0) {
                $count++;
            }

            $i++;
        }

        return $count <= 2 && $count != 0 ? self::$isPrime = true : self::$isPrime; 
    }

    private function isEven() :bool{
       return $this->number % 2 == 0 ? self::$isEven = true : self::$isEven;
    }

    private function isFibo() :bool{
        $i = 0;
        $fibo1 = 1;
        $fibo2 = 0;
        $result = 0;
        while ($i <  $this->number) {
            $result = $fibo1 + $fibo2;

            $fibo2 = $fibo1;

            $fibo1 = $result;
           $i++;

        }   
        return $result == $this->number ? self::$isFibo = true : self::$isFibo;
    }

    public function checkNumber() :string{
        $this->isPrime();

        $this->isEven();

        $this->isFibo();

        $this->message = "The number: " . $this->number . " ".  (self::$isPrime ? "is prime, " : "not is prime, ") . (self::$isFibo ? "is fibonacci, " : "not is fibonacci, ") . (self::$isEven ? "and is even \n" : "and is odd \n");

     return $this->message;
    }
}

/* $taste = new Pfe(-3); */ // This throw an Error
$taste = new Pfe(351);
echo $taste->checkNumber() . "\n";
$taste = new Pfe(54861);
echo $taste->checkNumber() . "\n";

$taste = new Pfe(124);
echo $taste->checkNumber() . "\n";

$taste = new Pfe(223);
echo $taste->checkNumber() . "\n";

$taste = new Pfe(9);
echo $taste->checkNumber() . "\n";

$taste = new Pfe(4);
echo $taste->checkNumber() . "\n";

/* $taste = new Pfe("hola");
echo $taste->checkNumber() . "\n"; */ // Another Error
?>