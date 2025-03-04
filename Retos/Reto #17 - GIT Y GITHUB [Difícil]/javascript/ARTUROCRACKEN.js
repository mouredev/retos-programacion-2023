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

const URL = `https://api.github.com/repos/mouredev/retos-programacion-2023/commits`;

async function getCommits(url) {
  try {
    const response = await fetch(url);
    const commits = await response.json();
    commits.slice(0, 10).forEach((commit, index) => {
      console.log(`Commit ${index + 1} | ${commit.sha} | ${commit.commit.author.name} | ${commit.commit.message} | ${new Date(commit.commit.author.date).toLocaleString()}\n\n`);
    });
  } catch (error) {
    console.error('Error fetching commits:', error);
  }
}

getCommits(URL);
