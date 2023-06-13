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

const getData = async (username, nameRepo, numberOfCommits) => {
    const url = `https://api.github.com/repos/${username}/${nameRepo}/commits`;
    const response = await fetch(url);
    const data = await response.json();

    const commits = data.slice(0, numberOfCommits).map((commit, index) => {
        const { sha, commit: { author: { name, date }, message } } = commit;
        const newDate = new Date(date).toLocaleString();
        return `Commit ${index + 1} | ${sha.slice(0, 7)} | ${name} | ${message} | ${newDate}`;
    }
    );
    return commits;

};

(async () => {
    const data = await getData("lemito66", "django-crud-react", 10);

    data.forEach(element => {
        console.log(element);
    });

})();