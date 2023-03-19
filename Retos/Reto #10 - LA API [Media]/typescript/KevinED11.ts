type PromiseResponse = Promise<void>
type CallApi = (endpoint: string) => PromiseResponse


const callApi: CallApi = async (endpoint: string): PromiseResponse => {
try {
    const response: Response = await fetch(endpoint)
    const data: JSON = await response.json()
    console.log(data)
} catch(error) {
    console.log(error)
}

}


// primera forma
callApi("https://rickandmortyapi.com/api/character") 




// segunda forma
try {
    fetch("https://rickandmortyapi.com/api/character")
    .then(response =>  response.json())
    .then(response => console.log(response))
    .catch(error => console.error(error))
} catch(error) {
      console.error(error)
}