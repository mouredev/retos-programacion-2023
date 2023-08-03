using Octokit;
using System.Text.RegularExpressions;

namespace Reto17;

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

class Program
{
    static void Main(string[] args)
    {
        GitLast10Commits("mouredev","retos-programacion-2023");
        //GitLast10Commits("JonAFernan","EjerciciosProgramacion" );
        Console.ReadKey();
    }

    static async void GitLast10Commits(string owner , string repository)
    {
        string token ="PersonalToken";
        int commitCounter = 1;
        GitHubClient client = new GitHubClient(new ProductHeaderValue("JonAFernan"));
        client.Credentials = new Credentials(token);
        
        IReadOnlyList<GitHubCommit> commits = await client.Repository.Commit.GetAll(owner, repository , new ApiOptions {PageCount = 1 , PageSize = 10 });

        foreach( GitHubCommit commit in commits)
        {
            System.Console.WriteLine($"Commit {commitCounter} | {commit.Sha} | {commit.Commit.Author.Name} | {Regex.Replace(commit.Commit.Message, @"\n", "")} | {commit.Commit.Committer.Date.ToString("g")}");
            commitCounter ++;

        }
    }
}
