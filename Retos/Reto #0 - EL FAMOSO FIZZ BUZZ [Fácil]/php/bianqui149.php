<?php
class getRet0
{
    public const Initial = 1;
    public const End     = 100;
    public const Fizz    = 3;
    public const Buzz    = 5;

    /**
     * It returns an array of numbers from 1 to 100, where each number is a multiple of the parameter
     * passed to the function.
     * 
     * @return array
     */
    public function getMultiple()
    {
        $list = array();

        for ( $i = self::Initial; $i <= self::End; $i++ ) {
            $isThree = ( $i % self::Fizz ) === 0;
            $isFive  = ( $i % self::Buzz ) === 0;
            $list[]  = ( $isThree && $isFive ? 'fizzbuzz' : ( $isThree ? 'fizz' : ( $isFive ? 'buzz' : $i ) ) ) . "\n";
        }

        return $list;
    }


    public function __toString()
    {
        $listReturn      = $this->getMultiple();
        $generatedOutput = implode( $listReturn );
        return $generatedOutput;
                
    }
}

$ret0 = new getRet0();

echo $ret0;