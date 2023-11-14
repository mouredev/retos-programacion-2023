<?php

declare (strict_types = 1);

$repoOwner = 'mouredev';
$repoName = 'retos-programacion-2023';

$apiUrl = "https://api.github.com/repos/$repoOwner/$repoName/commits";

$params = [
    'per_page' => 10,
];

$options = [
    'http' => [
        'method' => 'GET',
        'header' => "User-Agent: php",
    ],
];

$context = stream_context_create($options);
$response = file_get_contents("$apiUrl?" . http_build_query($params), false, $context);
$commits = json_decode($response, true);

foreach ($commits as $commit) {
    echo $commit['sha'] . '|' . $commit['commit']['author']['name'] . '|' . $commit['commit']['message'] . '|' . $commit['commit']['author']['date'], PHP_EOL;
}
