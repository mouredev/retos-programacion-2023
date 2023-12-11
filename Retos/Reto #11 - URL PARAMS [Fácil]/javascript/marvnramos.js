const url = 'https://retosdeprogramacion.com?year=2023&challenge=0';

/**
 * Get the parameters from a url and print them in the console
 * @param {*} url - The url to get the parameters from 
 */
const getParameters = (url) => {
    let index = url.indexOf('?');
    let values = [];

    for(let i = index + 1; i < url.length; i++) {
        let endIndex = url.indexOf('&', i);

        if(endIndex === -1) {
            endIndex = url.length;
        }

        let startIndex = url.lastIndexOf('=', endIndex);
        if(startIndex === -1) {
            startIndex = i;
        }

        values.push(url.slice(startIndex + 1, endIndex));
            
        // Update the index to skip the current parameter value
        i = endIndex;
    }
    console.log(values);
}

getParameters(url);