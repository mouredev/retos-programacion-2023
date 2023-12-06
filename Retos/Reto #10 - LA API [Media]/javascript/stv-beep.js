const DOG_FACT_API_ENDPOINT = "https://dog-api.kinduff.com/api/facts"

const request = () => {
    fetch(DOG_FACT_API_ENDPOINT)
    .then(res => res.json())
    .then(res => console.log(res.facts[0]))
}
request()
