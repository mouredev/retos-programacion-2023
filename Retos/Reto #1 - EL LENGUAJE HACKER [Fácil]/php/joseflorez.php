<?php

$lang = [
	'a' => '4',
	'b' => 'I3',
	'c' => '[',
	'd' => ')',
	'e' => '3',
	'f' => '|=',
	'g' => '&',
	'h' => '#',
	'i' => '1',
	'j' => ',_|',
	'k' => '>|',
	'l' => '1',
	'm' => '/\/\\',
	'n' => '^/',
	'o' => '0',
	'p' => '|*',
	'q' => '(_,)',
	'r' => 'I2',
	's' => '5',
	't' => '7',
	'u' => '(_)',
	'v' => '\/',
	'w' => '\/\/',
	'x' => '><',
	'y' => 'j',
	'z' => '2',
	'0' => 'o',
	'1' => 'L',
	'2' => 'R',
	'3' => 'E',
	'4' => 'A',
	'5' => 'S',
	'6' => 'b',
	'7' => 'T',
	'8' => 'B',
	'9' => 'g',
];

$text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.';

function printLeet($text, $lang) 
{
	print strtr($text, $lang) ."\n";
}

printLeet($text, $lang);

