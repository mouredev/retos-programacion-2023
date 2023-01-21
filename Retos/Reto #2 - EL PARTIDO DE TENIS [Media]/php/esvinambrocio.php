<?php

/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 *
 * Version: PHP 8.2
 */

class Player
{
    protected string $name;
    protected int $points = 0;
    protected bool $finished = false;

    public function __construct(string $name)
    {
        $this->name = strtoupper($name);
    }

    public function addPoints()
    {

        ++$this->points;
    }

    public function getPoints(): int
    {
        return $this->points;
    }
    public function reset():void
    {
        $this->finished = false;
        $this->points = 0;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function isFinished():bool
    {
        return $this->finished;
    }

    public function getTheWinner(Player $player):Player
    {
        $p1 = $this->getPoints();
        $p2 = $player->getPoints();
        return $p1 > $p2 ? $this : $player;
    }

    public function getFullMessage(Player $player):string
    {
        $p1 = $this->getPoints();
        $p2 = $player->getPoints();
        $message = "{$this->getMessage()} - {$player->getMessage()}";
        if(($p1 < 3 || $p2 < 3) && $p1 < 4 && $p2 < 4){
            return $message;
        }
        if(($p1 < 3 || $p2 < 3)){
            return "";
        }
        $winner = $this->getTheWinner($player);
        if(abs($p1-$p2) > 1){
            $this->finished = true;
            return "";
        }

        if($p1 == $p2){
            return "Deuce";
        }

        return "Ventaja {$winner->getName()}";
    }

    public function getMessage()
    {
        $messages = ['Love', 15, 30, 40];
        if (
            !in_array($this->points, array_keys($messages))
            && $this->points !== 0
        ) {
            return 40 - 3 + $this->points;
        }
        return $messages[$this->points];
    }
}

class Game
{
    const P1 = 'P1';
    const P2 = 'P2';

    /** @var Player[] $players */
    protected array $players;

    public function __construct()
    {
        $this->players = [
            Game::P1 => new Player(Game::P1),
            Game::P2 => new Player(Game::P2)
        ];
    }
    public function play(string ...$moves)
    {
        echo "----- Start ----- \n";
        foreach($moves as $key => $move) {
            if(!in_array($move, array_keys($this->players))){
                echo "El movimiento es invalido \n";
                break;
            }
            $p1 = $this->players[Game::P1];
            $p2 = $this->players[Game::P2];

            if($p1->isFinished() || $p2->isFinished()){
                echo "Los puntos jugados no son correctos \n";
                break;
            }

            $this->players[$move]->addPoints();

            $message = $p1->getFullMessage($p2);
            if(!empty($message)){
                echo "$message \n";
            }

            $isFinishedGame = ($key + 1) === count($moves);
            if($this->players[$move]->isFinished() && $isFinishedGame){
                echo "Ha ganado {$this->players[$move]->getName()} \n";
            }

        }

        if(!$p1->isFinished() && !$p2->isFinished()){
            echo "Los puntos jugados no son correctos \n";
        }
        foreach($this->players as $player){
            $player->reset();
        }

        echo "----- Finished ----- \n";
    }
}

$game = new Game();

$game->play(...[ 'P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
$game->play(...[ 'P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1', 'P2', 'P1']);
$game->play(...[ 'P1', 'P1', 'P1', 'P1', 'P1', 'P1']);
$game->play(...[ 'P1', 'P1']);

