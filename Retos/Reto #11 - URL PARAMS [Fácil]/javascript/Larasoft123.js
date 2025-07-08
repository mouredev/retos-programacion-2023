


url = "https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"




function getUrlParams(url) {
    const pattern = "[&|?]([a-zA-Z0-9._%-]+)=([a-zA-Z0-9._%-]+)"
    const answer = Array.from(url.matchAll(pattern))
    return answer.map((match) => {
        const [complete,key,value] = match
        return {complete,key,value}

    })



}




const params = getUrlParams(url)

console.log(params)