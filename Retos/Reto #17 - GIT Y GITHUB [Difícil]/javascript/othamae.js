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


function readCommits(repo) {

    return fetch(`https://api.github.com/repos/${repo}/commits`)
        .then(response => response.json())
        .then(data => {
            let commits = []
            for (let i = 0; i < 10; i++) {
                commits.push({
                    commit: i + 1,
                    Hash: data[i].commit.tree.sha,
                    Author: data[i].commit.author.name,
                    Message: data[i].commit.message,
                    Date: data[i].commit.author.date
                })
            }
            console.log(commits)
            return commits
        }).catch(error => console.log(error))

}


const repo = 'mouredev/retos-programacion-2023'

readCommits(repo)


