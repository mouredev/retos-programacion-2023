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

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Net;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace deathwing696
{
    class Deathwing696
    {
        static void Main()
        {
            string owner = "deathwing696";
            string repo = "retos-programacion-2023";
            int numberOfCommits = 10;

            try
            {
                List<GitHubCommit> commits = GetCommits(owner, repo, numberOfCommits);
                int i = 1;

                foreach (var commit in commits)
                {
                    Console.WriteLine($"Commit {i++} | {commit.Sha} | {commit.Commit.Author.Name} | {commit.Commit.Message} | {commit.Commit.Author.Date}");
                    Console.WriteLine();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }

            Console.Read();
        }

        static List<GitHubCommit> GetCommits(string owner, string repo, int numberOfCommits)
        {
            string apiUrl = $"https://api.github.com/repos/{owner}/{repo}/commits?per_page={numberOfCommits}";
            string mi_token = "mi_token";
            ServicePointManager.Expect100Continue = true;
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;            
            var wrGETURL = (HttpWebRequest)WebRequest.Create(apiUrl);
            wrGETURL.Method = "GET";
            wrGETURL.Headers.Add("Authorization", $"Bearer {mi_token}");
            wrGETURL.Accept = "application/json";
            wrGETURL.UserAgent = "deathwing696";

            try
            {
                using (WebResponse response = wrGETURL.GetResponse())
                {
                    using (Stream strReader = response.GetResponseStream())
                    {
                        if (strReader != null)
                        {
                            using (StreamReader objReader = new StreamReader(strReader))
                            {
                                string body = objReader.ReadToEnd();

                                return JsonConvert.DeserializeObject<List<GitHubCommit>>(body);
                            }                            
                        }
                        else
                        {
                            return new List<GitHubCommit>();
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return new List<GitHubCommit>();
            }
        }
    }

    public class GitHubCommit
    {
        [JsonProperty("sha")]
        public string Sha { get; set; }

        [JsonProperty("commit")]
        public GitHubCommitInfo Commit { get; set; }
    }

    public class GitHubCommitInfo
    {
        [JsonProperty("author")]
        public GitHubAuthorInfo Author { get; set; }

        [JsonProperty("message")]
        public string Message { get; set; }
    }

    public class GitHubAuthorInfo
    {
        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("date")]
        private string _date;

        public string Date
        {
            get
            {
                DateTime dt = DateTime.Parse(_date);

                return $"{dt.Day}/{dt.Month}/{dt.Year} {dt.Hour}:{dt.Minute}";
            }
            set
            {
                _date = value;
            }
        }
    }


}