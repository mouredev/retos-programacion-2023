<?php

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

class genPass
{
    private $length=16;
    private $useUppercase=false;
    private $useNumbers=false;
    private $useSymbols=false;
    const RANGES = [
        'symbols' => [
            'min' => 32,
            'max' => 47,
        ],
        'numbers' => [
            'min' => 48,
            'max' => 57,
        ],
        'upper' => [
            'min' => 65,
            'max' => 90
        ],
        'lower' => [
            'min' => 97,
            'max' => 122,
        ],
     ];

     private $resultingPass='';

     public function getPassLength(): int
     {
         return $this->length;
     }
     
     public function setPassLength($length): self
     {
         if ($length>16) {
             $this->length = 16;
         }
         if ($length<8) {
             $length=8;
         }
         $this->resultingPass = '';
         $this->length = $length;

         return $this;
     }

     public function getUseNumbers(): bool
     {
         return $this->useNumbers;
     }

     public function setUseNumbers($value): self
     {
         $this->useNumbers = $value;

         return $this;
     }
     
     public function getUseSymbols(): bool
     {
         return $this->useSymbols;
     }

     public function setUseSymbols($value): self
     {
         $this->useSymbols = (bool) $value;

         return $this;
     }
     
     public function getUseUppercase(): bool
     {
         return $this->useUppercase;
     }

     public function setUseUppercase($value): self
     {
         $this->useUppercase = (bool) $value;

         return $this;
     }

     public function genPassword()
     {
         $this->resultingPass='';
         $minOrd = 97; // La 'a'
         $maxOrd = self::RANGES['lower']['max'];
         if ($this->getUseUppercase()) {
             $minOrd = self::RANGES['upper']['min'];
         }
         if ($this->getUseNumbers()) {
             $minOrd = self::RANGES['numbers']['min'];
         }
         if ($this->getUseSymbols()) {
             $minOrd = self::RANGES['symbols']['min'];
         }
         while (strlen($this->resultingPass)<$this->getPassLength()) {
            $ord = rand($minOrd,$maxOrd);
            $valid = true;
            if ($ord>=self::RANGES['upper']['min'] && $ord<=self::RANGES['upper']['max']) {
                $valid = $this->getUseUppercase();
            } else {
                if ($ord>=self::RANGES['numbers']['min'] && $ord<=self::RANGES['numbers']['max']) {
                    $valid = $this->getUseNumbers();
                } else {
                    if ($ord>=self::RANGES['symbols']['min'] && $ord<=self::RANGES['symbols']['max']) {
                        $valid = $this->getUseSymbols();
                    }
                }
            }
            if ($valid) {
            $this->resultingPass[strlen($this->resultingPass)] = chr($ord);
            }
        }
        printf("Contraseña (%d): %s", $this->length, $this->resultingPass);
    }
}

$test = new genPass();
$test->setPassLength(10)
->setUseUppercase(true)
->setUseNumbers(true)
->setUseSymbols(false);
$test->genPassword();

$test->setPassLength(16)
->setUseUppercase(true)
->setUseNumbers(false)
->setUseSymbols(false);

$test->setPassLength(16)
->setUseUppercase(false)
->setUseNumbers(false)
->setUseSymbols(false);
$test->genPassword();
