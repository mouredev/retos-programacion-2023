function ImprimirValorParametros (url){
    url = url.split('?')[1].split('&');
    const array = url.map( value =>{
        return value.split("=")[1]
    });
    return array;
}

console.log(ImprimirValorParametros("https://retosdeprogramacion.com?year=2023&challenge=0"));
