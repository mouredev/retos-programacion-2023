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
 * 
 * REALIZADO POR LAURA ORTEGA - 05/09/2023
 */





async function LastNCommits(n) {
    try{

        const res = await fetch("https://api.github.com/repos/mouredev/retos-programacion-2023/commits");
        const data = await res.json();
        let commits = [];
        for (let i = 0; i < n; i++) {
            
            commits.push({
                commit: i + 1,
                Hash: data[i].commit.tree.sha.slice(0, 7),
                Autor: data[i].commit.author.name,
                Mensaje: data[i].commit.message,
                Fecha: new Date(data[i].commit.author.date).toLocaleString().toLocaleUpperCase(),
            });
        

            console.log(`Commit ${commits[i].commit} | ${commits[i].Hash} | ${commits[i].Autor} | ${commits[i].Mensaje.replace(/\n/g, " ")} | ${commits[i].Fecha}`);

        }

    }catch(error){
        console.log(error)
    }
}

LastNCommits(10)