import chalk from 'chalk'
import fetch from 'node-fetch'



const URL_STARSHIPS:string = 'https://swapi.dev/api/starships/'
/**
 * Interface que representa una nave espacial de Star Wars
 */
interface Starship {
    model:                  string;
    starship_class:         string;
    manufacturer:           string;
    cost_in_credits:        string;
    length:                 string;
    crew:                   string;
    passengers:             string;
    max_atmosphering_speed: string;
    hyperdrive_rating:      string;
    MGLT:                   string;
    cargo_capacity:         string;
    consumables:            string;
    pilots:                 string[];
    created:                Date;
    edited:                 Date;
    name:                   string;
    url:                    string;
}


/**
 * Función que obtiene las naves espaciales de Star Wars llamando a la API de Star Wars
 * @returns Promise<Array<Starship>>
 *     Promesa que resuelve con un array de naves espaciales
 *     Si hay algun error en la llamada a la API, la promesa se rechaza con el error
 */
function getStarships(): Promise<Array<Starship>> {
    return new Promise((resolve, reject) => {
        fetch(URL_STARSHIPS)
            .then((res:any) => res.json())
            .then((data:any) => {
                resolve(data.results)
            })
            .catch((err: any) => reject(err))

    })


}

/**
 * Llamada a la función getStarships() para obtener las naves espaciales de Star Wars
 * Las naves espaciales se muestran por consola con el nombre y la puntuación de hiperimpulsor
 */

getStarships().then(data => {
    console.log(chalk.green.bold("Starships Star Wars:"))
    console.log(chalk.green.bold("===================================="))
    data.forEach(starship => {
        const name:string = `${chalk.red.bold(starship.name)}-${chalk.blue.bold(starship.hyperdrive_rating)}`
        console.log(name)
    })
}).catch(err => {
    console.log(chalk.red.bold(err))
})




