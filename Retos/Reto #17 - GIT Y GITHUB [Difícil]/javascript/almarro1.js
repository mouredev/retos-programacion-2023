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

const GITHUB_API_URL = 'https://api.github.com';
const REPO_OWNER = 'mouredev';
const REPO_NAME = 'retos-programacion-2023';

const COMMITS_ENDPOINT = `/repos/${REPO_OWNER}/${REPO_NAME}/commits`;

const url = new URL(`${GITHUB_API_URL}${COMMITS_ENDPOINT}`);
url.search = new URLSearchParams({ per_page: 10, page: 1 }).toString()

fetch(url)
  .then((response) => response.json())
  .then((commits) => {
    commits.forEach((commit, index) => {
      console.log(`Commit ${index} | ${commit.sha} | ${commit.author.login} | ${commit.commit.message} | ${commit.commit.author.date}`);
    });
  })
  .catch((error) => console.error(error));

