<?php 
declare(strict_types=1);
$symbols = [
    "@","\\","*",".",",","{","}","-","_","#","$","%","/", "&","=","?","¿","<",">",
    "~","(",")","|","°"
];

$letters = [
'a' ,'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x' ,'y','z',
];
function genRamdonPassword(int $length) : string{
    global $letters;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
     $ranLetter = rand(0,count($letters) -1);
     $genPassword .= $letters[$ranLetter];  
    }
    return $genPassword;
}

function genPasswordWithNumber(int $length) : string{
    global $letters;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
        $ranNumber = rand(0,9);
        $ranLetter = rand(0,count($letters) -1);
        $randChoice = rand(0,1);

     $genPassword .= $randChoice == 0 ? strval($ranNumber) : $letters[$ranLetter];  
    }
    return $genPassword;
}
function genPasswordWithUpperCase(int $length) : string{
    global $letters;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
        $ranUpper = rand(0,count($letters) -1);
        $ranLetter = rand(0,count($letters) -1);
        $randChoice = rand(0,1);

     $genPassword .= $randChoice == 0 ? strtoupper($letters[$ranUpper]) : $letters[$ranLetter];  
    }
    return $genPassword;
}
function genPasswordWithSymbols(int $length) : string{
    global $letters, $symbols;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
        $ranSymbol = rand(0,count($symbols) -1);
        $ranLetter = rand(0,count($letters) -1);
        $randChoice = rand(0,1);

     $genPassword .= $randChoice == 0 ? $symbols[$ranSymbol] : $letters[$ranLetter];  
    }
    return $genPassword;
}

function genPasswordWithNumberSymbols(int $length) : string{
    global $letters, $symbols;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
        $ranSymbol = rand(0,count($symbols) -1);
        $ranNumber = rand(0,9);
        $ranLetter = rand(0,count($letters) -1);
        $randChoice = rand(0,2);
        if($randChoice == 0){
            $genPassword  .= $letters[$ranLetter]; 
            continue; 
        }
        
        if($randChoice == 1){

            $genPassword  .= $symbols[$ranSymbol];  
            continue; 
        }

        if($randChoice == 2){

            $genPassword  .= strval($ranNumber);  
            continue; 
        }
    }
    return $genPassword;

}

function genPasswordWithUpperSymbols(int $length) : string{
    global $letters, $symbols;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
        $ranSymbol = rand(0,count($symbols) -1);
        $ranLetter = rand(0,count($letters) -1);
        $randChoice = rand(0,2);
        if($randChoice == 0){
            $genPassword  .= $letters[$ranLetter]; 
            continue; 
        }
        
        if($randChoice == 1){

            $genPassword  .= $symbols[$ranSymbol];  
            continue; 
        }

        if($randChoice == 2){

            $genPassword  .=strtoupper($letters[rand(0,count($letters) - 1)]) ;  
            continue; 
        }
    }
    return $genPassword;
}

function genPasswordWithUpperNumber(int $length) : string{
    global $letters;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
        $ranNumber = rand(0,9);
        $ranLetter = rand(0,count($letters) -1);
        $randChoice = rand(0,2);
        if($randChoice == 0){
            $genPassword  .= $letters[$ranLetter]; 
            continue; 
        }

        if($randChoice == 1){
            $genPassword  .= intval($ranNumber); 
            continue; 
        }
        
        if($randChoice == 2){

            $genPassword  .=strtoupper($letters[rand(0,count($letters) - 1)]) ;  
            continue; 
        }
    }
    return $genPassword;
}
function genFullPassword(int $length) : string{
    global $letters, $symbols;
    $genPassword = "";
    for ($i=0; $i < $length ; $i++) { 
        $ranSymbol = rand(0,count($symbols) -1);
        $ranNumber = rand(0,9);
        $ranLetter = rand(0,count($letters) -1);
        $randChoice = rand(0,3);
        if($randChoice == 0){
            $genPassword  .= $letters[$ranLetter]; 
            continue; 
        }
        
        if($randChoice == 1){

            $genPassword  .= $symbols[$ranSymbol];  
            continue; 
        }

        if($randChoice == 2){

            $genPassword  .= strval($ranNumber);  
            continue; 
        }

        if($randChoice == 3){
            $genPassword  .= strtoupper($letters[rand(0,count($letters) - 1)]);  
            continue; 
        }
    }
    return $genPassword;
}

$length = intval(readline("Length of the password: "));

$isUpper = readline("With uppercase letters? write 1 for yes or 0 for no: ");
$withNumbers = readline("With numbers? write 1 for yes or 0 for no: ");
$withSymbols = readline("With Symbols? write 1 for yes or 0 for no: ");

if($length <= 0){
    $length = rand(8,16);
}

if ($length < 8 || $length > 16) {
    return exit("The values are very small or too big!!! \n");
}

if (empty($isUpper) || $isUpper == 0) {
    $isUpper = 0;
}else{

    $isUpper = 1;
}

if (empty($withNumbers) || $withNumbers == 0) {
    $withNumbers = 0;
}else{

    $withNumbers = 1;
}

if (empty($withSymbols) || $withSymbols == 0) {
    $withSymbols = 0;
}else{

    $withSymbols = 1;
}

if ($isUpper == 0 && $withNumbers == 0  && $withSymbols == 0 ) {
    $password = genRamdonPassword($length); 
    return print "Your password is: ". $password . " \n";   
}

if ($isUpper == 1 && $withNumbers == 0 && $withSymbols == 0) {
    $password = genPasswordWithUpperCase($length); 
    return print "Your password is: ". $password. " \n";   
}

if (!$isUpper && $withNumbers && !$withSymbols ) {
    $password = genPasswordWithNumber($length); 
    return print "Your password is: ". $password. " \n";   
}
if (!$isUpper && !$withNumbers && $withSymbols ) {
    $password = genPasswordWithSymbols($length); 
    return print "Your password is: ". $password. " \n";   
}
if ($isUpper && $withNumbers && $withSymbols ) {
    $password = genFullPassword($length); 
    return print "Your password is: ". $password. " \n";   
}

if (!$isUpper && $withNumbers && $withSymbols ) {
    $password = genPasswordWithNumberSymbols($length); 
    return print "Your password is: ". $password. " \n";   
}

if ($isUpper && !$withNumbers && $withSymbols ) {
    $password = genPasswordWithUpperSymbols($length); 
    return print "Your password is: ". $password. " \n";   
}

if ($isUpper && $withNumbers && !$withSymbols ) {
    $password = genPasswordWithUpperNumber($length); 
    return print "Your password is: ". $password. " \n";   
}
?>