const reto = (url: string) => {
    let params = url.split('?')[1].split('&')
    let values: string[] = []
    for (let param of params) {
        let value: string = param.split('=')[1]
        values.push(value);
    }
    console.log(values);
    return values;
}

reto("https://retosdeprogramacion.com?year=2023&challenge=0")
