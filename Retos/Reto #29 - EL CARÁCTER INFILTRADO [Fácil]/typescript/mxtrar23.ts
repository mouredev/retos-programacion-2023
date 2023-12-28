
/**
 * Funcion  para encontrar El carácter infiltrado
 * @param {string} firstText
 * @param {string} secondText
 */
const getFilteredCharacters = (firstText:string, secondText:string)  =>{
    let results : Array<string> = []

    if(!isLongSame(firstText,secondText)) throw Error ('Los textos son muy diferentes')

    for (let index = 0; index < firstText.length; index++) {
        if(firstText[index] !== secondText[index]){
            results.push(secondText[index])
        }  
    }

    printResults(firstText,secondText,results)
}


const isLongSame = (firstText:string, secondText:string) : boolean =>{
    const difference = Math.abs(firstText.length-secondText.length)
    if(difference>5) return false
    return true
}

const printResults = (firstText:string, secondText:string, results : Array<string>) => {
    if(results.length === 0) console.log('No hay caracteres filtrados ✅');
    
    console.log(`${firstText} / ${secondText} -> [${results}]`)
}



getFilteredCharacters('Hola a Todos, saludos desde Colombia','Hola a Todes, salados desda Columbia')
//Hola a Todos, saludos desde Colombia / Hola a Todes, salados desda Columbia -> [e,a,a,u]