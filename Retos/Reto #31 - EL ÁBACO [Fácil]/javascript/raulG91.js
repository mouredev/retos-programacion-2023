function abaco(array){

    let number = "";
    for(let i= 0;i < array.length; i++){

        let decimal_part = array[i].split("-")[0];
        number = number + decimal_part.length;

    }

    const number_format = new Intl.NumberFormat("es-ES");

    return number_format.format(number);


}
let input =["O---OOOOOOOO","OOO---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOOO---","---OOOOOOOOO"]

//let input =["---0OOOOOOOO","OOO0---OOOOOO","---OOOOOOOOO","OO---OOOOOOO","OOOOOOO---OO","OOOOOOOO---0","0--OOOOOOOOO"]

console.log("Numero en el abaco es: " + abaco(input))