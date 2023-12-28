<?php

/**
 * ¡Estoy de celebración! He publicado mi primer libro:
 * "Git y GitHub desde cero"
 * - Papel: mouredev.com/libro-git
 * - eBook: mouredev.com/ebook-git
 *
 * ¿Sabías que puedes leer información de Git y GitHub desde la gran
 * mayoría de lenguajes de programación?
 *
 * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 *
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 **/

class GitInfo
{
    private $_repo=null;
    private $_data=[];

    public function getRepo(): ?string
    {
        return $this->_repo;
    }

    public function setRepo($url): self
    {
        $this->_repo = $url;

        return $this;
    }

    private function getCommitURL(): ?string
    {
        if (null!=$this->getRepo()) {
            return $this->getRepo() . '/commits';
        }

        return null;
    }

    public function getCommits(int $number=10): array
    {
        $headerItems = [
            'Content-type:' => 'application/json',
            'Accept:' => 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'User-Agent:' => 'PHP',
        ];
        $header = "";
        foreach ($headerItems as $item => $value) {
            $header .= "$item $value\n";
        }
        $options = [
            "http" => [
                'method' => 'GET',
                'header' => $header
            ]
        ];
    
        $context = stream_context_create($options);
           $data = [];
        if (null!=$this->getCommitURL()) {
            $url = $this->getCommitURL() . '?per_page=' . $number;
            $this->_data = $data = json_decode(file_get_contents($url, false, $context), true);
        }

        return $data;
    }

    public function getCommitAuthor($commit)
    {
        return $commit['commit']['author']['name'];
    }

    public function getCommitDate($commit): string
    {
        $date = new DateTime($commit['commit']['author']['date']);

        return $date->format('d/m/Y H:i');
    }

    public function getCommitHash($commit)
    {
        return substr($commit['sha'], 0, 7);
    }

    public function getCommitMessage($commit)
    {
        return str_replace("\n", '', $commit['commit']['message']);
    }

}

$info = new gitInfo();
$commits = $info
    ->setRepo('https://api.github.com/repos/mouredev/retos-programacion-2023')
    ->getCommits(10);

$count = 0;
foreach ($commits as $commit) {
    $count++;
    printf(
        "Commit {%d} | %s | %s | %s | %s\n",
        $count,
        $info->getCommitHash($commit),
        $info->getCommitAuthor($commit),
        $info->getCommitMessage($commit),
        $info->getCommitDate($commit)
    );

}
        