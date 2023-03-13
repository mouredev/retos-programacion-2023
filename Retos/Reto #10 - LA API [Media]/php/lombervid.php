<?php

declare(strict_types=1);

function request(string $url, string $method = 'GET'): string|bool
{
    return file_get_contents($url, false, stream_context_create([
        'http' => [
            'method' => $method,
            'header' => 'Content-type: application/json',
        ],
    ]));
}

// Main code
$url = 'https://animechan.vercel.app/api/random';
echo request($url) . PHP_EOL;
