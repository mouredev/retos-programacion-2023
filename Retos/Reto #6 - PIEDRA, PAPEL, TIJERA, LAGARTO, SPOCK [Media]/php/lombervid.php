<?php

declare(strict_types=1);

enum Options: string
{
    case Rock = '🗿';
    case Paper = '📄';
    case Scissors = '✂️';
    case Lizard = '🦎';
    case Spock = '🖖';

    protected function priority(): array
    {
        return match ($this) {
            self::Rock => [self::Lizard, self::Scissors],
            self::Paper => [self::Rock, self::Spock],
            self::Scissors => [self::Paper, self::Lizard],
            self::Lizard => [self::Spock, self::Paper],
            self::Spock => [self::Scissors, self::Rock],
            default => [],
        };
    }

    public function wins(Options $option): bool
    {
        return in_array($option, $this->priority());
    }

    public static function toString()
    {
        return implode(' | ', array_column(self::cases(), 'value'));
    }
}

class GameOptions implements IteratorAggregate
{
    protected array $options = [];

    public function __construct(array $options = null)
    {
        if ($options) {
            $this->setOptions($options);
        }
    }

    public function setOptions(array $options)
    {
        $newOptions = [];

        foreach ($options as $key => $option) {
            if (!is_array($option)) {
                throw new InvalidArgumentException("Every option must be an array on key '{$key}'");
            }

            try {
                $newOptions[] = [Options::from($option[0] ?? null), Options::from($option[1] ?? null)];
            } catch (Throwable $t) {
                throw new InvalidArgumentException("Options must be of type (at index {$key}): " . Options::toString());
            }
        }

        $this->options = $newOptions;
    }

    public function getIterator(): Traversable
    {
        return new ArrayIterator($this->options);
    }
}

class LizardSpockGame
{
    protected int $score1 = 0;
    protected int $score2 = 0;

    public function __construct(
        protected GameOptions $options = new GameOptions(),
    ) {
    }

    public function setInput(array $options)
    {
        $this->options->setOptions($options);

        return $this;
    }

    public function play(): string
    {
        $this->resetScores();

        foreach ($this->options as [$p1, $p2]) {
            if ($p1->wins($p2)) {
                $this->score1 += 1;
            } elseif ($p2->wins($p1)) {
                $this->score2 += 1;
            }
        }

        if ($this->score1 === $this->score2) {
            return 'Tie';
        }

        return ($this->score1 > $this->score2) ? 'Player 1' : 'Player 2';
    }

    protected function resetScores()
    {
        $this->score1 = 0;
        $this->score2 = 0;
    }
}

/**
 * Test cases
 *
 * Rock     = '🗿'
 * Paper    = '📄'
 * Scissors = '✂️'
 * Lizard   = '🦎'
 * Spock    = '🖖'
 *
 */

$failures = 0;
$tests = [
    [
        [['🗿','✂️'], ['✂️','🗿'], ['📄','✂️']],
        'Player 2',
    ],
    [
        [['🖖','✂️'], ['📄','🗿'], ['✂️', '🦎'], ['🖖', '🦎'], ['📄', '🗿']],
        'Player 1',
    ],
    [
        [['🖖', '🖖']],
        'Tie',
    ],
    [
        [['🖖', '🗿'], ['🦎', '✂️'], ['📄', '🖖'], ['🦎', '🗿']],
        'Tie',
    ],
];

$game = new LizardSpockGame();

foreach ($tests as $index => [$input, $want]) {
    try {
        $got = $game->setInput($input)->play();

        if ($got !== $want) {
            $failures += 1;
            echo "Test {$index} failed: got \"{$got}\", want \"{$want}\"" . PHP_EOL;
        } else {
            echo $got . PHP_EOL;
        }
    } catch (Throwable $t) {
        $failures += 1;
        echo "Test {$index} failed with message: " . $t->getMessage() . PHP_EOL;
    }
}

if ($failures === 0) {
    echo "All tests complete successfuly" . PHP_EOL;
}
