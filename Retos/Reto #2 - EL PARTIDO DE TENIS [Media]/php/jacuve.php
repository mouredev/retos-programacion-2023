<?php

class TenisGame
{

    private $points;
    private $status;
    private $pointsP1;
    private $pointsP2;

    private const POINTS_TEXTS = ['Love', '15', '30', '40', 'Adv', 'Deuce', 'Game'];
    private const INDEX_ADVENTAGE = 4;
    private const INDEX_DEUCE = 5;
    private const INDEX_GAME = 6;

    public function __construct(array $points)
    {
        $this->points = $points;
        $this->pointsP1 = 0;
        $this->pointsP2 = 0;
    }
    
    public function showPoints(): string
    {
        $result = '';
        foreach ( $this->points as $point){
            $result .= ' . ' .$this->processPoint($point);
        }
        return $result;
    }

    private function processPoint(string $point)
    {
        if ($point === 'P1') {
            $this->sumarPuntoP1();
            $marcador = $this->obtenerMarcador();
            return $marcador;
        }

        if ($point === 'P2') {
            $this->sumarPuntoP2();
            $marcador = $this->obtenerMarcador();
            return $marcador;
        }

    }

    private function sumarPuntoP1()
    {
        if ($this->pointsP1 === 0){
            $this->pointsP1 = 1;
        } elseif ($this->pointsP1 === 1){
            $this->pointsP1 = 2;
        } elseif ($this->pointsP1 === 2){
            $this->pointsP1 = 3;
        } elseif ($this->pointsP1 >= 3){
            $this->pointsP1 += 1;
        }
    }


    private function sumarPuntoP2()
    {
        if ($this->pointsP2 === 0){
            $this->pointsP2 = 1;
        } elseif ($this->pointsP2 === 1){
            $this->pointsP2 = 2;
        } elseif ($this->pointsP2 === 2){
            $this->pointsP2 = 3;
        } elseif ($this->pointsP2 >= 3){
            $this->pointsP2 += 1;
        }
    }

    private function obtenerMarcador(): string
    {
        $resultado = '';
        if ($this->pointsP1 <= 3 && $this->pointsP2 <=3) {
    $resultado = self::POINTS_TEXTS[$this->pointsP1] . '-' . self::POINTS_TEXTS[$this->pointsP2];
        } else {
            if ($this->pointsP1 > $this->pointsP2 && $this->pointsP1 - $this->pointsP2 === 2) {
                $resultado = self::POINTS_TEXTS[self::INDEX_GAME] . ' P1';
            } else if ($this->pointsP1 > $this->pointsP2 && $this->pointsP1 - $this->pointsP2 === 1) {
                $resultado = self::POINTS_TEXTS[self::INDEX_ADVENTAGE] . ' P1';
            } else if ($this->pointsP1 < $this->pointsP2 && $this->pointsP2 - $this->pointsP1 === 2) {
                $resultado = self::POINTS_TEXTS[self::INDEX_GAME] . ' P2';
            } elseif ($this->pointsP1 < $this->pointsP2 && $this->pointsP2 - $this->pointsP1 === 1) {                
                $resultado = self::POINTS_TEXTS[self::INDEX_ADVENTAGE] . ' P2';
            } else {
                $resultado = ' ' . self::POINTS_TEXTS[self::INDEX_DEUCE];
            }
        }
        return $resultado;
    }
}
echo 'Juego tenis.;
echo "\n";
$juego = new TenisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
echo  'Resultado : ' . $juego->showPoints();