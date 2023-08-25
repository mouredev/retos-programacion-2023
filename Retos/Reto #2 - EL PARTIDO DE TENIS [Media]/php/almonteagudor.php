<?php

enum Score
{
    case LOVE;
    case FIFTEEN;
    case THIRTY;
    case FORTY;
    case ADVANTAGE;
    case WINNER;

    public function value(): string
    {
        return match ($this) {
            Score::LOVE => "Love",
            Score::FIFTEEN => "15",
            Score::THIRTY => "30",
            Score::FORTY => "40",
            Score::ADVANTAGE => "Ventaja",
            Score::WINNER => "Ganador",
        };
    }
}

class Player
{
    private Score $score = Score::LOVE;

    public function getScore(): Score
    {
        return $this->score;
    }

    public function setScore(Score $score): void
    {
        $this->score = $score;
    }

    public function __toString(): string
    {
        return $this->score->value();
    }
}

class ScoreBoard
{
    private const P1 = "P1";
    private const P2 = "P2";

    /**
     * @var string[]
     */
    private array $score = [];

    /**
     * @var Player[]
     */
    private array $players = [];

    public function __construct()
    {
        $this->players[self::P1] = new Player();
        $this->players[self::P2] = new Player();
    }

    /**
     * @throws Exception
     */
    public function playGame($pointsWon): array
    {
        foreach ($pointsWon as $pointWon) {
            $this->pointWon($pointWon);
        }

        return $this->score;
    }

    /**
     * @throws Exception
     */
    private function pointWon(string $player): void
    {
        if (!isset($this->players[$player])) {
            throw new Exception("El jugador indicado no existe");
        }

        $this->score[] = $this->addPoint($player);
    }

    /**
     * @throws Exception
     */
    private function addPoint(string $player): string
    {
        $pointedPlayer = $this->players[$player];
        $unpointedPlayer = $this->players[$player === self::P1 ? self::P2 : self::P1];

        if ($pointedPlayer->getScore() === Score::FORTY && $unpointedPlayer->getScore() === Score::FORTY) {
            $pointedPlayer->setScore(Score::ADVANTAGE);
            return $pointedPlayer . " " . $player;
        }

        if ($pointedPlayer->getScore() === Score::FORTY && $unpointedPlayer->getScore() === Score::ADVANTAGE) {
            $unpointedPlayer->setScore(Score::FORTY);
            return "Deuce";
        }

        if ($pointedPlayer->getScore() === Score::THIRTY && $unpointedPlayer->getScore() === Score::FORTY) {
            $pointedPlayer->setScore(Score::FORTY);
            return "Deuce";
        }

        $pointedPlayer->setScore(
            match ($pointedPlayer->getScore()) {
                Score::LOVE => Score::FIFTEEN,
                Score::FIFTEEN => Score::THIRTY,
                Score::THIRTY => Score::FORTY,
                Score::FORTY, Score::ADVANTAGE => Score::WINNER,
                Score::WINNER => throw new Exception("El jugador ya había ganado, se han jugado puntos de más")
            }
        );

        if ($pointedPlayer->getScore() === Score::WINNER) {
            return $pointedPlayer . " " . $player;
        }

        return $this->players[self::P1] . " - " . $this->players[self::P2];
    }
}

function play(string $name, array $pointsWon)
{
    $scoreBoard = new ScoreBoard();

    try {
        $score = $scoreBoard->playGame($pointsWon);

        echo("********** {$name} *********\n");

        foreach ($score as $scoreLine) {
            echo($scoreLine . "\n");
        }

        echo("******************************\n");
    } catch (Exception $e) {
        echo($e->getMessage() . "\n");
    }
}

play("PARTIDO 1", ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]);
play("PARTIDO 2", ["P1", "P1", "P1", "P1"]);
play("PARTIDO 3", ["P2", "P2", "P2", "P2"]);
play("PARTIDO 4", ["P2", "P2", "P2", "P1", "P1", "P1", "P1", "P1"]);
play("PARTIDO 5", ["P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2", "P1", "P2", "P2"]);




