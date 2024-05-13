/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
const root = "https://www.dnd5eapi.co/api/spells/animal-shapes";


const getSpells = async (url: string): PromiseResponse => {
    let spells: any = {name: "", description: ""};

    try {
        const res: Response = await fetch(url);
        const data: JSON = await res.json();

        spells.name = data.name
        spells.description = data.desc[0]
    } catch (error) {
        console.log(error);
    };

    return spells;
};

getSpells(root);