<?php

    function GameStart($attempts)
    {
        echo "COMENZEMOS A JUGAR: \n";
        do {
            echo "****************************************** \n";
            echo "* Adivina la palabra que estoy pensando: * \n";
            echo "****************************************** \n";
            $secretWord = ChooseWord();
            $secretWord = ClearDiacritic($secretWord);
            $wordToShow = HiddenChars($secretWord);
            $result = PlayGame($secretWord, $wordToShow, $attempts);
            if($result)
                echo "Has ganado! \n";
            else{
                echo "Has perdido! \n";
                echo "La palabra era: $secretWord \n";
            }
            echo "Quieres seguir jugando? (n para salir, cualquier otra para seguir) \n";
            $answer = readline();
        } while($answer != "n");
        
    }

    function HiddenChars($word)
    {
        $charsToHidde = round(strlen($word) * 0.6);
        $totalHidde = 0;

        while($totalHidde < $charsToHidde)
        {
            $pos = rand(1, strlen($word)) - 1;
            if($word[$pos] != "_")
            {
                $word[$pos] = "_";
                $totalHidde++;
            }
        }
        return $word;
    }

    function PlayGame($realWord, $hiddenWord, $attempts)
    {
        $tries = 1;
        $success = false;

        do {
            echo "Intento $tries de $attempts \n";
            echo "Palabra: ". strtoupper($hiddenWord). "\n";
            echo "Introduce una letra: \n";
            $letter = readline();
            $letter = trim($letter);
            if (strlen($letter) == 1)
                $hiddenWord = CheckLetter($realWord, $hiddenWord, $letter);
            else
                $success = CheckWord($realWord, $letter);
            
            $tries++;
            echo "--------------------------------\n";
        } while($tries <= $attempts && !$success);

        return $success;
    }

    function CheckLetter($word, $secretWord, $letterToCheck)
    {
        $letterToCheck = strtolower($letterToCheck);
        $word = strtolower($word);
        $secretWord = strtolower($secretWord);
        $pos = strpos($word, $letterToCheck);
        if($pos !== false)
        {
            $secretWord[$pos] = $letterToCheck;
            $pos = strpos($word, $letterToCheck, $pos + 1);
            while($pos !== false)
            {
                $secretWord[$pos] = $letterToCheck;
                $pos = strpos($word, $letterToCheck, $pos + 1);
            }
        }
        else
        {
            echo "La letra $letterToCheck no está en la palabra \n";
        }
        return $secretWord;
    }

    function CheckWord($word, $secretWord)
    {
        $success = false;
        if($word == $secretWord)
            $success = true;
        return $success;
    }

    function ChooseWord()
    {
        $url = "https://random-word-api.herokuapp.com/word?lang=es";

        $datos = file_get_contents($url);
        $datosDecodificados = json_decode($datos);
        $palabra = $datosDecodificados[0];
        return $palabra;
    }

    function ClearDiacritic($word) 
    {
        $clearWord = str_replace(
            array('á', 'é', 'í', 'ó', 'ú', 'ü', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ü'),
            array('a', 'e', 'i', 'o', 'u', 'u', 'A', 'E', 'I', 'O', 'U', 'U'),
            $word
        );
        
        return $clearWord;
    }

    $attempts = 5;
    GameStart($attempts);
?>