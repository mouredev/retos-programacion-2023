using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Octokit;
namespace _48
{
    /*
 * Todo llega a su fin... Este es el último reto de programación 
 * semanal de 2023.
 *
 * Crea un programa que muestre un listado calculado en tiempo real
 * con todos los usuarios que han resuelto algún reto de programación
 * de este año.
 * - El listado debe estar ordenado por el número de ejercicios resueltos
 *   por cada usuario (y mostrar ese contador al lado de su nombre).
 * - También se debe de mostrar el número de usuarios que han participado
 *   y el número de correcciones enviadas.
 *
 * Muchísimas gracias por ayudar a crear este gran recurso
 * para la comunidad... ¡Prepárate para 2024!   
 */
    internal class Program
    {
        static async Task Main(string[] args)
        {
            var github = new GitHubClient(new ProductHeaderValue("Reto48"));

            // Autenticación si es necesaria
            github.Credentials = new Credentials("pega_tu_token");

            var desdeFecha = new DateTimeOffset(new DateTime(2023, 12, 01));//Lo pongo en Diciembre para que cargue menos commits y se aprecie más rápido
            var hastaFecha = DateTimeOffset.UtcNow;

            Console.WriteLine($"Obteniendo commits desde: {desdeFecha} hasta: {hastaFecha}");

            var commits = await github.Repository.Commit.GetAll("mouredev", "retos-programacion-2023",
                    new CommitRequest
                    {
                        Since = desdeFecha,
                        Until = hastaFecha
                    });
            var totalCommits = commits.Count;
            var commitsObtenidos = 0;

            Console.WriteLine($"Número total de commits a cargar: {totalCommits}");

            var usuarios = new Dictionary<string, int>();
            int commitSinAutor = 0;
            foreach (var commit in commits)
            {
                commitsObtenidos++;
                var porcentajeCompletado = (double)commitsObtenidos / totalCommits * 100;
                Console.Write($"\rProgreso: [{new string('#', (int)(porcentajeCompletado / 5))}{new string('-', (int)((100 - porcentajeCompletado) / 5))}] {porcentajeCompletado:F2}%");
                await Task.Delay(10);
                var autor = commit.Author?.Login; // Se agrega ? para verificar si el autor es nulo

                if (!string.IsNullOrEmpty(autor))//si el commit tiene autor:
                {
                    if (usuarios.ContainsKey(autor))//verifica si el autor existe en el diccionario
                    {
                        usuarios[autor]++;//Si existe le agrega 1
                    }
                    else
                    {
                        usuarios.Add(autor, 1);//Si no existe lo crea y asigna 1 de valor inicial
                    }
                }
                else
                {
                    commitSinAutor++;
                }
            }
            Console.WriteLine();
            Console.WriteLine($"Commits sin autor : {commitSinAutor}");
            Console.WriteLine("Usuarios que han resuelto retos de programación en 2023:");

            foreach (var usuario in usuarios.OrderByDescending(u => u.Value))
            {
                Console.WriteLine($"{usuario.Key}: {usuario.Value} ejercicios resueltos");
            }

            Console.WriteLine($"Número de usuarios que han participado: {usuarios.Count}");
            Console.WriteLine($"Número total de correcciones enviadas: {commits.Count}");
            Console.ReadKey();
        }
    }
}
