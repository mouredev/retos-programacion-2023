const URL_BASE = "https://pokeapi.co/api/v2/pokemon/";

async function getPokemon(pokemon) {
    await fetch(URL_BASE + pokemon)
    .then(res => res.json())
    .then(pokeRes => {
        console.log({
        id: pokeRes.id,
        name: pokeRes.name,
        height: pokeRes.height,
        weight: pokeRes.weight
        });
    });
}

getPokemon("pikachu"); // by Name   output: { id: 25, name: 'pikachu', height: 4, weight: 60 }