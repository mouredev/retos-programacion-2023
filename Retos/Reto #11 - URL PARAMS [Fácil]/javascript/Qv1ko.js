getParameters("https://retosdeprogramacion.com?year=2023&challenge=0");

function getParameters(url) {

    let parameters = []
    const splits = url.split("&")

    if (splits.length > 1) {
        for (let i = 0; i < splits.length; i++) {
            if (splits[i].split("=").length == 2) {
                parameters.push('"' + splits[i].split("=")[1] + '"')
            }
        }
        console.log(parameters.toString())
    } else {
        console.log("The URL has no parameters")
    }
    
}
