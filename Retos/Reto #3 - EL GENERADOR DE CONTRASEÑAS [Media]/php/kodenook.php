<?php

declare(strict_types=1);

/**
 * The function generates a random password of a specified length, with optional inclusion of uppercase
 * letters, numbers, and symbols.
 *
 * @param long The "long" parameter specifies the length of the password to be generated. It is an
 * optional parameter and if not provided, a random length between 8 and 16 characters will be chosen.
 * @param bool caps A boolean parameter that determines whether the password should include uppercase
 * letters or not. If set to true, the password may include uppercase letters. If set to false, the
 * password will only include lowercase letters.
 * @param bool numbers The "numbers" parameter determines whether or not to include numbers in the
 * generated password. If set to true, numbers will be included. If set to false, numbers will not be
 * included.
 * @param bool symbols A boolean parameter that determines whether symbols should be included in the
 * password. If set to true, symbols such as !, @, #, etc. will be included in the password. If set to
 * false, symbols will not be included.
 *
 * @return string a string that represents a randomly generated password.
 */
function password(?int $long, bool $caps = false, bool $numbers = false, bool $symbols = false): string
{
    $password = '';
    $characters = range(97, 122);

    if ($caps) {
        $characters = array_merge(range(65, 90), $characters);
    }
    if ($numbers) {
        $characters = array_merge(range(48, 57), $characters);
    }
    if ($symbols) {
        $characters = array_merge(range(33, 47), range(58, 64), range(91, 96), $characters);
    }
    if (is_null($long)) {
        $long = rand(8, 16);
    }

    for ($i = 0; $i < $long - 1; $i++) {
        $password .= chr($characters[rand(0, count($characters) - 1)]);
    }

    return $password;
}

/* The line `echo password(null, true, true, true);` is calling the `password` function and passing in
the following arguments: */
echo password(null, true, true, true);
