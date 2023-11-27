const url = 'https://retosdeprogramacion.com?year=2023&challenge=0';

const getParameters = (url) => {
    let index = url.indexOf('?');
    let values = [];
    for(let i = index + 1; i < url.length; i++) {
        if(url[i] === '&'){
            values.push(url.slice(index + 1, i));
            index = i;
        }
    }
    console.log(values);
}

getParameters(url);

// let example = 'hola mundo'
// for(let i = 5; i <= example.lastIndexOf('o'); i++) {
//     console.log(example[i])
// }

