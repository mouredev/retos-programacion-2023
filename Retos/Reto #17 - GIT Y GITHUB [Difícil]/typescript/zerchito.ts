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
type RepositoryCommit ={
  hash: string,
  author: string,
  message: string,
  date: Date
}
const repositoryName = 'mouredev/retos-programacion-2023';
const NUMBER_OF_COMMITS = 10;
async function readCommits(repositoryName: string):Promise<RepositoryCommit[]> {
  const url = `https://api.github.com/repos/${repositoryName}/commits`
  let commitsData = await fetch(url)
      .then(response => response.json())
      .catch(error => console.log(error));
  let commits = commitsData.slice(0, NUMBER_OF_COMMITS);
  commits = commits.map(commitInfo => {
    return {
      hash: commitInfo.commit.tree.sha,
      author: commitInfo.commit.author.name,
      message: commitInfo.commit.message,
      date: new Date(commitInfo.commit.author.date)
    }
  });
  console.log(commits)
  return commits;
}

readCommits(repositoryName);
