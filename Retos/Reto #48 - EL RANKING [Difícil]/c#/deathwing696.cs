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

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using Octokit;

namespace reto48
{
    public class Conteo
    {
        public string Nombre_usuario { get; set; }
        public int Num_veces { get; set; }

        public Conteo(string nombre_usuario)
        {
            Nombre_usuario = nombre_usuario;
            Num_veces = 1;
        }
    }
    public class Reto48
    {
        static async Task Main()
        {
            string owner = "mouredev"; 
            string repo = "retos-programacion-2023"; 
            string token = "Mi_token_de_github"; 
            string mainFolder = "Retos"; 
            string branch = "main"; 
            List<Conteo> aportaciones = new List<Conteo>();
            int i = 1;

            var github = new GitHubClient(new ProductHeaderValue("deathwing696"));
            github.Credentials = new Credentials(token);

            var reference = await github.Git.Reference.Get(owner, repo, $"heads/{branch}");
            var encodedMainFolder = Uri.EscapeDataString(mainFolder);
            var contents = await github.Repository.Content.GetAllContentsByRef(owner, repo, encodedMainFolder, reference.Object.Sha);

            await ProcessContentsAsync(github, owner, repo, contents, branch, aportaciones);

            aportaciones = aportaciones.OrderByDescending(conteo => conteo.Num_veces).ToList();

            foreach (var usuario in aportaciones)
            {
                Console.WriteLine($"{i}:El usuario {usuario.Nombre_usuario} ha participado {usuario.Num_veces} veces");
                i++;
            }

            Console.ReadKey();
        }

        static async Task ProcessContentsAsync(GitHubClient github, string owner, string repo, IReadOnlyList<RepositoryContent> contents, string branch, List<Conteo> aportaciones)
        {
            foreach (var content in contents)
            {
                if (content.Type == ContentType.Dir)
                {                    
                    var decodedSubfolderPath = Uri.UnescapeDataString(content.Path);                    
                    var subfolderContents = await github.Repository.Content.GetAllContentsByRef(owner, repo, decodedSubfolderPath, branch);
                    await ProcessContentsAsync(github, owner, repo, subfolderContents, branch, aportaciones);
                }
                else if (content.Type == ContentType.File)
                {                    
                    var username = System.IO.Path.GetFileNameWithoutExtension(content.Name);

                    if (!aportaciones.Any(conteo => conteo.Nombre_usuario == username))
                    { 
                        Conteo usuario = new Conteo(username);
                        aportaciones.Add(usuario);
                    }
                    else
                    {
                        Conteo usuario = aportaciones.Find(conteo => conteo.Nombre_usuario == username);

                        usuario.Num_veces++;
                    }
                }
            }
        }
    }
}