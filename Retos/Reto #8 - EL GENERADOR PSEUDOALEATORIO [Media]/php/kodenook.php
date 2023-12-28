<?php

declare(strict_types=1);

/**
 * The function returns a random integer between 0 and 100.
 *
 * @return int a random integer between 0 and 100.
 */
function random(): int
{
    return time() % 101;
}

echo random();
