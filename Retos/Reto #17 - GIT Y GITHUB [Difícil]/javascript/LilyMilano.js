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

const repo = 'mouredev/retos-programacion-2023';

async function retrieveCommits(repo, numberOfCommits = 10) {
	try {
		const response = await fetch(`https://api.github.com/repos/${repo}/commits`);
		const data = await response.json();
		const commits = [];
		for (let i = 0; i < numberOfCommits; i++) {
			commits.push({
				commit: i + 1,
				Hash: data[i].commit.tree.sha,
				Author: data[i].commit.author.name,
				Message: data[i].commit.message,
				Date: data[i].commit.author.date,
			});
			console.log(
				`Commit: ${commits[i].commit} | ${commits[i].Hash} | ${commits[i].Author} | ${commits[i].Message} | ${commits[i].Date}`
			);
		}
		return commits;
	} catch (error) {
		console.error(error);
	}
}
retrieveCommits(repo,10);
