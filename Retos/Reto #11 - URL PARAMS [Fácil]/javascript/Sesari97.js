function getParameters(url) {
    
    var url = url.split('?')[1];
    var parameters = [];


    for (var i in url.split('&')){
        var parameter = url.split('&')[i].split('=')[1];
        parameters.push(parameter)
    }
    return parameters;
    }
    
    console.log(getParameters('https://retosdeprogramacion.com?year=2023&challenge=0'))