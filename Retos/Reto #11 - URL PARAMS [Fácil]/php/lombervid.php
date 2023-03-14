<?php

declare(strict_types=1);

class URL
{
    protected string $url;

    public function __construct(string $url)
    {
        $this->url = $this->validateURL($url);
    }

    public function getQueryParams(): array
    {
        $params = [];

        if (!$paramsString = $this->getParametersString()) {
            return $params;
        }

        foreach (explode('&', $paramsString) as $param) {
            $pairs = explode('=', $param, 2);
            $params[$pairs[0]] = $pairs[1] ?? true;
        }

        return $params;
    }

    protected function getParametersString(): string|false
    {
        $query = explode('?', $this->url);

        if (!isset($query[1])) {
            return false;
        }

        return trim($query[1]) ?: false;
    }

    protected function validateURL(string $url): string
    {
        $url = trim($url);

        if (!filter_var($url, FILTER_VALIDATE_URL)) {
            throw new Exception("Invalid URL", 1);
        }

        return $url;
    }
}

// Test cases
$test = [
    [
        'https://retosdeprogramacion.com?year=2023&challenge=0',
        ['year' => '2023', 'challenge' => 0],
    ],
    [
        'http://google.com/?something=',
        ['something' => ''],
    ],
    [
        'http://google.com/?something',
        ['something' => true],
    ],
    [
        'http://google.com/?',
        [],
    ],
];

$arrToStr = function ($arr) {
    $str = '[';
    $index = 1;
    $len = count($arr);

    foreach ($arr as $key => $value) {
        $str .= "{$key} => {$value}";

        if ($index++ < $len) {
            $str .= ", ";
        }
    }

    return $str . ']';
};

foreach ($test as $key => [$url, $want]) {
    $got = (new URL($url))->getQueryParams();

    if ($got != $want) {
        echo "Failed test {$key}: got {$arrToStr($got)}, want {$arrToStr($want)}" . PHP_EOL;
    }
}
