<?php

class PlayGame{

    private $puntos;
    private $estado;
    private $playerOne;
    private $playerTwo;

    private const POINT_SET = ['Love','15','30','40','Adventage','Deuce','Game'];
    private const ADVENTAGE = 4;
    private const DEUCE = 5;
    private const GAME = 6;

    public function __construct(array $puntos){
        $this->puntos = $puntos;
        $this->playerOne = $playerOne = 0;
        $this->playerTwo = $playerTwo = 0;
    }

    public function getPoints(): string{
        $res = '';
        foreach ($this->puntos as $puntos){
            $res .= ' . ' . $this->getProcess($puntos);
        }
        return $res;
    }

    private function getProcess(string $puntos){
        if( $puntos === 'P1'){
            $this->addPointPlayers($puntos);
            $mark = $this->getMark();
            return $mark;
        }else if( $puntos === 'P2'){
            $this->addPointPlayers($puntos);
            $mark = $this->getMark();
            return $mark;
        }
    }

    private function addPointPlayers(string $player){
        if($player === 'P1'){
            if($this->playerOne === 0){
                $this->playerOne = 1;
            }else if($this->playerOne === 1){
                $this->playerOne = 2;
            }else if($this->playerOne === 2){
                $this->playerOne = 3;
            }else if($this->playerOne >= 3){
                $this->playerOne += 1;
            }
        }else if($player === 'P2'){
            if($this->playerTwo === 0){
                $this->playerTwo = 1;
            }else if($this->playerTwo === 1){
                $this->playerTwo = 2;
            }else if($this->playerTwo === 2){
                $this->playerTwo = 3;
            }else if($this->playerTwo >= 3){
                $this->playerTwo += 1;
            }
        }
    }

    private function getMark(): string{
        $res = '';
        if($this->playerOne <= 3 && $this->playerTwo <= 3){
            $res = self::POINT_SET[$this->playerOne]. '-' .self::POINT_SET[$this->playerTwo];
        }else{
            if($this->playerOne > $this->playerTwo && $this->playerOne - $this->playerTwo === 2){
                $res = self::POINT_SET[self::GAME]. ' P1';
            }else if($this->playerOne > $this->playerTwo && $this->playerOne - $this->playerTwo === 1){
                $res = self::POINT_SET[self::ADVENTAGE]. ' P1';
            }else if($this->playerOne < $this->playerTwo && $this->playerOne - $this->playerTwo === 2){
                $res = self::POINT_SET[self::GAME]. ' P2';
            }else if($this->playerOne < $this->playerTwo && $this->playerOne - $this->playerTwo === 1){
                $res = self::POINT_SET[self::ADVENTAGE]. ' P2';
            }else{
                $res = ' '. self::POINT_SET[self::DEUCE];
            }
        }
        return $res;
    }

}

echo 'Play Game ';
echo ' ';
$game = new PlayGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
echo 'Resultado: '. $game->getPoints();