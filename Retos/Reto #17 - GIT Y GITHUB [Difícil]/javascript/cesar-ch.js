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


async function CommitList() {
    const url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"
    const res = await fetch(url)
    const data = await res.json()
    let list = ''

    for (let i = 0; i < 10; i++) {
        list += `* Commit ${i + 1} | ${data[i].commit.tree.sha.slice(0, 7)} | ${data[i].commit.author.name} | ${data[i].commit.message.replace(/\n/g, ' ')} | ${new Date(data[i].commit.author.date).toLocaleString()}\n`
    }

    console.log(list)
}

CommitList()