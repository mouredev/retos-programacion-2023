getParameters("https://retosdeprogramacion.com?year=2023&challenge=0");

function getParameters(url: string) {

    let parameters: string[] = [];
    const splits = url.split("?")[1].split("&");
    let keyValue: string[] = []

    if (splits.length > 0) {
        for (let i = 0; i < splits.length; i++) {
            keyValue = splits[i].split("=");
            if (keyValue.length === 2) {
                parameters.push(`"${keyValue[1]}"`);
            }
        }
        console.log(parameters.join(", "));
    } else {
        console.log("The URL has no parameters");
    }

}
