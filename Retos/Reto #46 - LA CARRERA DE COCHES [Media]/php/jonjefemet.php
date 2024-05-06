<?php

declare(strict_types=1);

enum PositionType
{
    case GOAL;
    case ROAD;
    case OBSTACLE;
}

class RaceTrack
{

    private $trackLines = [];
    private int $tracklength;

    /** @var Car[] $cars */
    private array $cars;

    private function __construct(int $tracklength, Car ...$cars)
    {
        $this->tracklength = $tracklength;
        $this->cars = $cars;
    }

    private function makePosition(string $item, PositionType $positionType)
    {
        return [
            "item" => $item,
            "positionType" => $positionType
        ];
    }

    private function canHaveObstacle(): bool
    {
        $probability = rand(1, 100);

        return $probability <= 20;
    }

    private function build()
    {

        foreach ($this->cars as  $car) {

            $totalTrees = rand(1, 3);
            $trackLine[] = $this->makePosition("🏁", PositionType::GOAL);
            for ($i = 0; $i < $this->tracklength; $i++) {

                $canHaveObstacle = ($this->canHaveObstacle() and $totalTrees > 0);
                if ($canHaveObstacle) {
                    $totalTrees--;
                }
                [$item, $positionType] = match ($canHaveObstacle) {
                    true => ["🌲", PositionType::OBSTACLE],
                    false => ["_", PositionType::ROAD],
                };
                $trackLine[] = $this->makePosition($item, $positionType);
            }

            $this->trackLines[$car->getId()] = $trackLine;
            $trackLine = [];
        }
    }

    private function findCarById(string $id): Car
    {
        $filtered = array_filter($this->cars, function (Car $car) use ($id) {
            return $car->getId() === $id;
        });

        return reset($filtered);
    }

    function showCurrentPositions(): void
    {
        foreach ($this->trackLines as $id => $cars) {
            print_r("\n");
            $car = $this->findCarById($id);

            foreach ($cars as $index => $trackLine) {

                $position = $this->tracklength - $index;
                $drawCar = $position === $car->getPosition();
                $item = match ($drawCar) {
                    true => $car->draw(),
                    false => $trackLine["item"],
                };
                print_r($item);
            }
        }
    }

    function nextTurn()
    {
        $winners = [];
        foreach ($this->cars as $car) {
            $car->move($this->tracklength);
            $currentPosition = $this->tracklength - $car->getPosition();

            $item = $this->trackLines[$car->getId()][$currentPosition];

            $positionType = $item["positionType"];
            $crash = function () use ($car) {
                if ($car->getStatus() === CarStatus::DRIVE) {
                    $car->crash();
                } else {
                    $car->drive();
                }
            };

            match ($positionType) {
                PositionType::OBSTACLE => $crash(),
                PositionType::GOAL => $car->stop(),
                default => ""
            };

            if ($positionType === PositionType::GOAL) {
                $winners[] = $car->draw();
            }
        }

        return $winners;
    }


    static function create(int $tracklength, Car ...$cars): RaceTrack
    {
        $raceTrack = new RaceTrack($tracklength + 1, ...$cars);
        $raceTrack->build();
        return $raceTrack;
    }
}

enum CarStatus
{
    case CRASH;
    case STOP;
    case DRIVE;
}

class Car
{

    private string $id;
    private string $player;
    private int $position;

    private CarStatus $status;

    private function __construct(string $id, string $player, CarStatus $status, int $position)
    {
        $this->id = $id;
        $this->player = $player;
        $this->status = $status;
        $this->position = $position;
    }

    function draw(): string
    {
        if ($this->status === CarStatus::CRASH) return "💥";

        return $this->player;
    }

    function getId(): string
    {
        return $this->id;
    }

    function crash()
    {
        $this->status = CarStatus::CRASH;
    }

    function stop()
    {
        $this->status = CarStatus::STOP;
    }

    function drive()
    {
        $this->status = CarStatus::DRIVE;
    }

    function getStatus(): CarStatus
    {
        return $this->status;
    }

    function getPosition(): int
    {
        return $this->position;
    }

    function move(int $tracklength)
    {
        if ($this->status === CarStatus::DRIVE) {
            $total = rand(1, 3);
            $this->position = $this->position + $total;
            if ($this->position >= $tracklength) {
                $this->position = $tracklength;
            }
        }
    }


    static function create(string $player): Car
    {
        return new Car(uniqid(), $player, CarStatus::DRIVE, 0);
    }
}

class Race
{
    private RaceTrack $raceTrack;

    private array $winners = [];

    private function __construct(RaceTrack $raceTrack)
    {
        $this->raceTrack = $raceTrack;
    }

    function cls()
    {
        print("\033[2J\033[;H");
    }

    function start()
    {
        $this->raceTrack->showCurrentPositions();

        while (!$this->existWinners()) {
            sleep(1);
            $winners = $this->raceTrack->nextTurn();
            $this->raceTrack->showCurrentPositions();
            if (count($winners) > 0) {
                $this->winners = $winners;
            }
        }

        print_r("\n");
        print_r("winners:");
        print_r($this->winners);
    }

    private function existWinners(): bool
    {
        return (bool) count($this->winners);
    }

    static function create(RaceTrack $raceTrack): Race
    {
        return new Race($raceTrack);
    }
}


$playeOne = Car::create("🚙");
$playeTwo = Car::create("🚗");
$raceTrack = RaceTrack::create(10, $playeOne, $playeTwo);
$race = Race::create($raceTrack);
$race->start();
