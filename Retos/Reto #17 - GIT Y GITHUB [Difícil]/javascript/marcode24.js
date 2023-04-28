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

const getCommits = ({ user, repo, limit = 10 }) => {
  const url = `https://api.github.com/repos/${user}/${repo}/commits?per_page=${limit}`;
  return fetch(url)
    .then((res) => res.json())
    .then((commits) => commits.map((commit, i) => {
      const { author } = commit.commit;
      const message = commit.commit.message.replace(/\n/g, '');
      const { name, date } = author;
      const sha = commit.sha.slice(0, 7);
      const newDate = new Date(date).toLocaleString();
      return `Commit ${i + 1} | ${sha} | ${name} | ${message} | ${newDate}`;
    }))
    .catch((err) => `Error: ${err}`);
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
getCommits("mouredev", "retos-programacion-2023")