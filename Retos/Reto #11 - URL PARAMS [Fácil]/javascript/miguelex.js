const FindParameters = (url) => {
    const params = [];

    const urlDividida = url.split("?");

    if (urlDividida.length > 1) {
        const listaParams = urlDividida[1].split("&");
        for (let i = 0; i < listaParams.length; i++) {
            const clearParam = listaParams[i].split("=");
            if (clearParam.length > 1 && clearParam[1] !== "") {
                params.push(clearParam[1]);
            } else {
                return "La cadena no tiene parametros validos";
            }
        }

        return params;
    } else {
        return "La cadena no tiene parametros";
    }
};

console.log(FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0"));
console.log(FindParameters("https://retosdeprogramacion.com"));
console.log(FindParameters("https://retosdeprogramacion.com?"));
console.log(FindParameters("https://retosdeprogramacion.com?year=2023"));
console.log(FindParameters("https://retosdeprogramacion.com?year=2023&"));
console.log(FindParameters("https://retosdeprogramacion.com?year=&"));
console.log(
FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python")
);