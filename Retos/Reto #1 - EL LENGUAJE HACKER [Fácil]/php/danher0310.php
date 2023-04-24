<?php

function changeText($texto){
  $dictionary = array(
    "a"=>"4",
    "b"=>"I3",
    "c"=>"[",
    "d"=>")",
    "e"=>"3",
    "f"=>"|=",
    "g"=>"&",
    "h"=>"#",
    "i"=>"1",
    "j"=>",_|",
    "k"=>">|",
    "l"=>"1",
    "m"=>"/\\/\\",
    "n"=>"^/",
    "o"=>"0",
    "p"=>"|*",
    "q"=> "(_,)",
    "r"=>"I2",
    "s"=>"5",
    "t"=>"7",
    "u"=>"(_)",
    "v"=>"\\/",
    "w"=>"\\/\\/",
    "x"=>"><",
    "y"=>"j",
    "z"=>"2",
    "1"=>"L",
    "2"=>"R",
    "3"=>"E",
    "4"=>"A",
    "5"=>"5",
    "6"=>"b",
    "7"=>"T",
    "8"=>"B",
    "9"=>"g",
    "0"=>"0",
    
  );
  $newtext = "";
  for($i = 0; $i < strlen($texto); $i++){
   
    if(isset($dictionary[$texto[$i]])){
      $newtext.= $dictionary[$texto[$i]];
    }else{
      $newtext.= $texto[$i];

    };
 
  }; 
  return $newtext;
};

$text = readline("Introduzca el texto a encruptar: ");
print(changeText($text));
?>