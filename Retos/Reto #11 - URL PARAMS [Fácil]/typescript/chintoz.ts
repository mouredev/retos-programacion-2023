export function printUrlParameters(url: String) {
    const parameters: string = url.substring(url.indexOf("?") + 1, url.length);
    const parametersArray: string[] = parameters.split("&")
    parametersArray.forEach(s => {
        const param : string[] = s.split("=")
        console.log(`Clave: ${param[0]} Valor: ${param[1]}`)
    })
}

printUrlParameters("mydomain.com/example/?pagina=1&sortOrder=price&sortOrder=’lowToHigh’")
