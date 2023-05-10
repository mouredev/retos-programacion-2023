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

import fetch from 'node-fetch'
import chalk from 'chalk'


/**
 * Interface que representa un commit de GitHub
 */
interface ICommit{
    sha: string;
    commit: {
        author: {
            name: string;
            date: string;
            email: string;
        }
        message: string;

    }
}


/**
 * Clase para manejar la API de GitHub
 * @param repositoryName Nombre del repositorio
 */
class GitHub {

    repositoryName: string;
    GIT_HUB_URL = 'https://api.github.com/repos/';
    constructor(repositoryName: string) {
        this.repositoryName = repositoryName;

    }

    /**
     * Método para leer los commits de un repositorio
     * @param commits Número de commits a leer
     * @returns Array de commits
     */
    async readCommits(commits: number): Promise<Array<ICommit>> {

        return new Promise((resolve, reject) => {
            const url = `${this.GIT_HUB_URL}${this.repositoryName}/commits?per_page=${commits}`
            fetch(url)
                .then((res: any) => res.json())
                .then((data: Array<ICommit>) => {
                    resolve(data)
                })
                .catch((err: any) => reject(err))

        })
    }

    /**
     * Método para imprimir los commits
     * @param commits Array de commits a imprimir
     */
    printCommit(commits:ICommit[]) {
        commits.forEach((commit, index) => {
            const hash = commit.sha.slice(7);
            const {name, date} = commit.commit.author;
            const msg = commit.commit.message;
            console.log(`${chalk.green.bold(
                `Commit ${index + 1}`)} | ${chalk.red(hash)} | ${chalk.blue(name)} | ${chalk.cyan(msg)} | ${chalk.yellow(new Date(
                    date
                ).toLocaleString())} |`
            )
        })


    }


}

/**
 * Ejecución del programa
 */

const repositoryName = 'mouredev/retos-programacion-2023';
const github = new GitHub(repositoryName);
const commits = await github.readCommits(10);
github.printCommit(commits);




