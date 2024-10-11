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

const url =
  'https://api.github.com/repos/mouredev/retos-programacion-2023/commits';

const request = async () => {
  try {
    const gitHubRequest = await fetch(url, {
      method: 'GET',
    });
    const jsonResponse = await gitHubRequest.json();
    return jsonResponse;
  } catch (err) {
    throw new Error(`❌❌❌ ${err}`);
  }
};

const response = async () => {
  const jsonData = await request();
  for (let i = 0; i < 10; i++) {
    console.log(
      `Commit ${i + 1} | ${jsonData[i].sha.slice(0, 7)} | ${
        jsonData[i].commit?.author?.name
      } | ${jsonData[i].commit?.message.slice(0, 30)} | ${new Date(
        jsonData[i].commit?.author?.date
      ).toLocaleString()}`
    );
  }
};

const main = () => {
  response();
};

main();
