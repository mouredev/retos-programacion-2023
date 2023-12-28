interface Character {
    id: number
    name: string
    status: string
    species: string

}

interface Response {
    results: Character[]
}

function getCharacters(): Promise<Response> {
    return fetch('https://rickandmortyapi.com/api/character')
        .then(res => res.json())
        .then(res => {
            return res as Response
        })
}

export function retrieveCharacters(): void {
    console.log("Pidiendo los personajes de la serie Rick y Morty ...")
    getCharacters().then(r => console.log(r.results.map(c => c.name)))
}

retrieveCharacters()
