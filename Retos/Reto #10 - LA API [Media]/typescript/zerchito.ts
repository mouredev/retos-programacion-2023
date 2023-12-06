/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */

type AnimeData = {
  title: string;
  type: string;
  score: number;
  synopsis: string;
  url: string;
};

class APICaller {
  #url: string;

  constructor(url: string) {
    this.#url = url;
  }

  async callURL(url?: string): Promise<AnimeData[]| void> {
    this.#url = url ?? this.#url;
    const animeList = await fetch(this.#url)
      .then(data => data.json())
      .then(data => {
        const animeList: any[] = data.data;
        const response: AnimeData[] = animeList.map(anime => {
          return {
            title: anime.title,
            type: anime.type,
            score: anime.score,
            synopsis: anime.synopsis,
            url: anime.url,
          };
        });
        console.log(response);
        return response;
      })
      .catch(error => {
        console.log('Unexpected error:' + error);
      });
    return animeList;
  }
}

const url = 'https://api.jikan.moe/v4/anime?q=naruto&sfw';
const caller = new APICaller(url);
console.log(caller.callURL());