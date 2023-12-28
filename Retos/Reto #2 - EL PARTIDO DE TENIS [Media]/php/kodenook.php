<?php

declare(strict_types=1);

/* The Player class represents a player in a tennis game and provides methods to manage their points. */
class Player
{
    /**
     * The function is a constructor for a PHP class that initializes a private property called
     * "points" with a default value of 'Love'.
     */
    function __construct(
        private $points = 'Love',
    ) {
    }

    /**
     * The function "getPoints" returns a string representing the points.
     * 
     * @return string a string value.
     */
    function getPoints(): string
    {
        return $this->points;
    }

    /**
     * The function "addPoint" increments the points of a player in a tennis game.
     */
    function addPoint(): void
    {
        $this->points = match ($this->getPoints()) {
            'Love' => '15',
            '15' => '30',
            '30' => '40'
        };
    }

    /**
     * The function "resetPoints" sets the value of the variable "points" to 'Love'.
     */
    function resetPoints(): void
    {
        $this->points = 'Love';
    }
}

/* The `tennisMatch` class is a PHP class that simulates a game of tennis between two players and
determines the winner. */
class tennisMatch
{
    /**
     * The function is a constructor for a PHP class with four private properties.
     */
    function __construct(
        private $Deuce = null,
        private $winner = null,
        private $advantage = null,
    ) {
    }

    /**
     * The function "play" simulates a game of tennis between two players and determines the winner.
     * 
     * @param Player p1 Player 1, an instance of the Player class.
     * @param Player p2  is an instance of the Player class.
     */
    function play(Player $p1, Player $p2): void
    {
        while (is_null($this->winner)) {
            $random = rand(1, 2);

            if ($random === 1) {
                if (!is_null($this->Deuce)) {
                    if (is_null($this->advantage)) {
                        $this->advantage = $p1;
                    } elseif ($this->advantage === $p2) {
                        $this->advantage = null;
                    } else {
                        $this->winner = $p1;
                    }
                } else {
                    if ($p1->getPoints() === '40') {
                        $this->winner = $p1;
                    } else {
                        $p1->addPoint();
                    }
                }
            } else {
                if (!is_null($this->Deuce)) {
                    if (is_null($this->advantage)) {
                        $this->advantage = $p2;
                    } elseif ($this->advantage === $p1) {
                        $this->advantage = null;
                    } else {
                        $this->winner = $p2;
                    }
                } else {
                    if ($p2->getPoints() === '40') {
                        $this->winner = $p2;
                    } else {
                        $p2->addPoint();
                    }
                }
            }

            $this->deuce($p1, $p2);

            echo $this->result($p1, $p2), PHP_EOL;
        }

        $p1->resetPoints();
        $p2->resetPoints();
    }

    /**
     * The function checks if both players have a score of '40' and sets the 'Deuce' property to true.
     * 
     * @param Player p1 An instance of the Player class representing the first player.
     * @param Player p2 The parameter  is an instance of the Player class.
     */
    function Deuce(Player $p1, Player $p2): void
    {
        if ($p1->getPoints() === '40' && $p2->getPoints() === '40') {
            $this->Deuce = true;
        }
    }

    /**
     * The function returns the result of a game between two players in the form of a string.
     * 
     * @param Player p1 An instance of the Player class representing player 1.
     * @param Player p2 Player 2
     * 
     * @return string a string that represents the result of a game between two players. The possible
     * return values are:
     */
    function result(Player $p1, Player $p2): string
    {
        $result = '';
        if (!is_null($this->winner)) {
            if ($this->winner === $p1)
                $result = 'Ha ganado el P1';
            else {
                $result = 'Ha ganado el P2';
            }
        } elseif (is_null($this->Deuce)) {
            $result = sprintf('%d - %d', $p1->getPoints(), $p2->getPoints());
        } else {
            if ($this->advantage === $p1) {
                $result = 'Ventaja P1';
            } elseif ($this->advantage === $p2) {
                $result = 'Ventaja P2';
            } else {
                $result = 'Deuce';
            }
        }

        return $result;
    }
}

/* The code is creating two instances of the `Player` class, `p1` and `p2`. It then creates an
instance of the `tennisMatch` class called `game`. Finally, it calls the `play` method of the
`game` object, passing in `p1` and `p2` as arguments. This simulates a game of tennis between the
two players and determines the winner. */
$p1 = new Player();
$p2 = new Player();
$game = new tennisMatch();
$game->play($p1, $p2);
