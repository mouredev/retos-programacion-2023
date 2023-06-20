/*
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
 * 
 */

<?php

    //Código creado a partir del GIST de travstoll ubicado en esta página -> https://gist.github.com/travstoll/d6d72855b4184fbfc30f3a20a9adbb4c

	//Auth Token para hacer uso del API (Añadir el tuyo creado previamente)
	$token = "Añade tu Access Personal Token que puedes crear desde GitHub";
	
	$url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits?per_page=10";

	//Añadir la información necesaria para el uso de API (método y headers)
	$opts = [
		'http' => [
				'method' => 'GET',
				'header' => [
						'User-Agent: PHP',
                        'Authorization: Bearer ' . $token,
                        'X-GitHub-Api-Version: 2022-11-28',
						'Content-type: application/x-www-form-urlencoded',
                ],
		]
	];

	//Inicializa file_get_contents
	$context = stream_context_create($opts);
	
	//Realiza el request a la página
	$content = file_get_contents($url, false, $context);
	
	//Convierte la información en Array
	$response_array = json_decode($content, true);	
	
    $commit_number = array('commit' => 0);

    //Luego de obtener la información del API podremos comenzar a obtener los datos de los commits
    foreach($response_array as $commit) {

        $commit_number['commit'] = $commit_number['commit'] + 1;

        $sha = substr($commit['sha'], 0, 7);
        $author_name = $commit['commit']['author']['name'];
        $message = str_replace("\n", '', $commit['commit']['message']);
        $time = date_format(date_create($commit['commit']['author']['date']), 'd/m/Y H:i');

        echo "Commit {$commit_number['commit']} | " . $sha . " | " . $author_name . " | " . $message . " | " . $time . "\n";
        
    }

?>
