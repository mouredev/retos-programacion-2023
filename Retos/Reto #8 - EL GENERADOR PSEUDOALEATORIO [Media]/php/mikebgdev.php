<?php

declare(strict_types=1);

function random (): int
{
    return hrtime(true) % 101;
}

echo random(). PHP_EOL;
echo random();

?>