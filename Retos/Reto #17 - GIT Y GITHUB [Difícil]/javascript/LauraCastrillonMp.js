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

async function getCommits() {
    try {
        const response = await fetch(`https://api.github.com/repos/mouredev/retos-programacion-2023/commits`);
        const data = await response.json();
        let commits = [];
        for (let i = 0; i < 10; i++) {
            commits.push({
                commit: i + 1,
                Hash: data[i].commit.tree.sha.slice(0, 7),
                Autor: data[i].commit.author.name,
                Mensaje: data[i].commit.message,
                Fecha: data[i].commit.author.date
            });
            let mensaje = commits[i].Mensaje.replace(/\n/g, " "); // Para eliminar el salto de linea que hay en el mensaje del commit
            console.log(`Commit: ${commits[i].commit} | ${commits[i].Hash} | ${commits[i].Autor} | ${mensaje} | ${commits[i].Fecha}`);
        }
    } catch (error) {
        return console.log(error);
    }
}

getCommits()


