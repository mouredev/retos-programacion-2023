# Reto #2: EL PARTIDO DE TENIS
#### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

## Enunciado

/*
* Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
* El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
* gane cada punto del juego.
*
* - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
* - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
* 15 - Love
* 30 - Love
* 30 - 15
* 30 - 30
* 40 - 30
* Deuce
* Ventaja P1
* Ha ganado el P1
* - Si quieres, puedes controlar errores en la entrada de datos.
* - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
*/

<?php



class Game
{

    public $players = [
        'P1' => [
            'puntuacion' => 'love',
            'rondas_ganadas' => 0
        ],
        'P2' => [
            'puntuacion' => 'love',
            'rondas_ganadas' => 0
        ]
    ];
    public $rondas;
    public $points = [0 =>0 , 1 => 15, 2=> 30 , 3=> 40, 'deuce' => 0];
    public $fin = false;


    function score($player)
    {
        $aux_score = $this->players[$player]['puntuacion'];
        $this->players[$player]['rondas_ganadas']++;
        $this-> rondas++;
        if($this->players[$player]['rondas_ganadas'] < 4)
        {
            $this->players[$player]['puntuacion'] = $this -> points[$this->players[$player]['rondas_ganadas']];
        }

        if ($this->players[$player]['puntuacion'] >= 40)
        {
            if($this->players['P1']['puntuacion'] ==  $this->players['P2']['puntuacion']  && $this->players['P1']['puntuacion'] >=40 )
            {
                if(($this->players[$player]['rondas_ganadas'] - ($this -> rondas / 2)) == 0.5 ){
                    return "Ventaja $player";
                }
                if(($this->players[$player]['rondas_ganadas'] - ($this -> rondas / 2)) == 1 ){
                    return "Gano $player";
                }
                return "Deuce";
            }
            if($aux_score == 40){
                if($this->players['P1']['puntuacion'] == 40)
            {
                $this->fin = true;
                return "Gano P1";
            }
            if($this->players['P2']['puntuacion'] == 40)
            {
                $this->fin = true;
                return "Gano P2";
            }
            }
            
        }
    }
        
    function start($secuencia)
    {
        foreach ($secuencia as $point_for) {
            $mensaje = $this->score($point_for);
            print("Ronda: " . $this->rondas . "\n");
            if($this->rondas < 6){
               
            }
            print "Punto para $point_for \n";
            print($this->players['P1']['puntuacion'] . " - " . $this->players['P2']['puntuacion'] . "\n");
            print($this->players['P1']['rondas_ganadas'] . " - " . $this->players['P2']['rondas_ganadas'] . "\n");
            print($mensaje . "\n");
            print("----------------------\n");
            if($this-> fin == true){
                break;
            }
        }
    }
}

$secuencia = ['P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2' , 'P1' , 'P1'  ];
$game = new Game();
$game->start($secuencia);
